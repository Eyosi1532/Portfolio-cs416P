#popgen

import argparse, random, re, wave
import numpy as np
import sounddevice as sd

# Constants
NAMES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
NOTE_NAMES = {s: i for i, s in enumerate(NAMES)}

def parse_note(s):
    note_name_re = re.compile(r"([A-G]b?)(\[([0-8])\])?")
    m = note_name_re.fullmatch(s)
    if m is None:
        raise ValueError("Invalid note format")
    s = m[1].capitalize()
    q = 4
    if m[3] is not None:
        q = int(m[3])
    return NOTE_NAMES[s] + 12 * q

def parse_linear_knob(k):
    v = float(k)
    if v < 0 or v > 10:
        raise ValueError
    return v / 10

def parse_db(d):
    v = float(d)
    if v > 0:
        raise ValueError
    return 10**(v / 20)

ap = argparse.ArgumentParser()
ap.add_argument('--bpm', type=int, default=90)
ap.add_argument('--samplerate', type=int, default=48000)
ap.add_argument('--root', type=parse_note, default="C[5]")
ap.add_argument('--bass-octave', type=int, default=2)
ap.add_argument('--balance', type=parse_linear_knob, default="5")
ap.add_argument('--gain', type=parse_db, default="-3")
ap.add_argument('--waveform', choices=['sine', 'square', 'saw', 'triangle'], default='sine')
ap.add_argument('--chord-loop', type=str, default="8,5,6,4")
ap.add_argument('--melody-range', type=str, default="C[4]-C[6]")
ap.add_argument('--output')
args = ap.parse_args()

# Functions for waveform generation
def generate_waveform(waveform, freq, samples):
    t = np.linspace(0, 1, samples, endpoint=False)
    if waveform == "sine":
        return np.sin(2 * np.pi * freq * t)
    elif waveform == "square":
        return np.sign(np.sin(2 * np.pi * freq * t))
    elif waveform == "saw":
        return 2 * (t * freq - np.floor(1 / 2 + t * freq))
    elif waveform == "triangle":
        return 2 * np.abs(2 * (freq * t - np.floor(freq * t + 0.5))) - 1

# Envelope
def apply_envelope(sound, attack=0.1, decay=0.1, sustain=0.8, release=0.1):
    length = len(sound)
    env = np.ones(length)
    attack_samples = int(length * attack)
    decay_samples = int(length * decay)
    release_samples = int(length * release)
    sustain_samples = length - attack_samples - decay_samples - release_samples

    env[:attack_samples] = np.linspace(0, 1, attack_samples)
    env[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain, decay_samples)
    env[-release_samples:] = np.linspace(sustain, 0, release_samples)
    return sound * env

# Rhythm track
def create_rhythm_track(samplerate, beats, bpm):
    beat_samples = int(samplerate / (bpm / 60))
    total_samples = beat_samples * beats
    rhythm = np.zeros(total_samples)
    noise = np.random.uniform(-1, 1, beat_samples // 4)  # Noise for rhythm
    
    for i in range(beats):
        start = i * beat_samples
        end = start + beat_samples // 4
        rhythm[start:end] = noise  # Add noise to the start of each beat
    
    return rhythm

# Main loop
beat_samples = int(np.round(args.samplerate / (args.bpm / 60)))
chord_loop = [int(x) for x in args.chord_loop.split(",")]
melody_range = [parse_note(n) for n in args.melody_range.split("-")]

sound = np.array([], dtype=np.float64)
for c in chord_loop:
    chord_root = c - 1
    melody = np.concatenate([
        apply_envelope(generate_waveform(args.waveform, 440 * 2 ** ((chord_root + random.randint(-3, 3)) / 12), beat_samples))
        for _ in range(4)
    ])
    bass = apply_envelope(generate_waveform(args.waveform, 440 * 2 ** ((chord_root - args.bass_octave * 12) / 12), beat_samples * 4))

    rhythm = create_rhythm_track(args.samplerate, 4, args.bpm)
    melody_gain = args.balance
    bass_gain = 1 - melody_gain

    combined = melody_gain * melody + bass_gain * bass + 0.1 * rhythm
    sound = np.append(sound, combined)

# Output or play
if args.output:
    output = wave.open(args.output, "wb")
    output.setnchannels(1)
    output.setsampwidth(2)
    output.setframerate(args.samplerate)
    data = args.gain * 32767 * sound.clip(-1, 1)
    output.writeframesraw(data.astype(np.int16))
    output.close()
else:
    sd.play(args.gain * sound, samplerate=args.samplerate, blocking=True)
