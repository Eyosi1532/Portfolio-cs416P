import argparse
import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy.signal import lfilter
import signal
import sys

def signal_handler(sig, frame):
    print("\nProgram interrupted! Exiting gracefully...")
    sd.stop()  # Stop any ongoing audio playback
    sys.exit(0)

# Register the signal handler for graceful exit
signal.signal(signal.SIGINT, signal_handler)

def apply_volume(data, volume_factor):
    """Adjust volume."""
    return np.clip(data * volume_factor, -1.0, 1.0)

def apply_bass(data, bass_gain):
    """Boost bass frequencies."""
    b = [0.2]
    a = [1, -bass_gain]
    return lfilter(b, a, data)

def apply_delay(data, rate, delay_sec, decay_factor):
    """Apply a delay effect."""
    delay_samples = int(rate * delay_sec)
    delayed = np.zeros(len(data) + delay_samples)
    delayed[:len(data)] = data
    for i in range(delay_samples, len(delayed)):
        delayed[i] += delayed[i - delay_samples] * decay_factor
    return delayed[:len(data)]

def apply_reverb(data, rate, reverb_decay):
    """Apply a reverb effect."""
    decay_samples = int(rate * reverb_decay)
    for i in range(decay_samples, len(data)):
        data[i] += data[i - decay_samples] * 0.3
    return np.clip(data, -1.0, 1.0)

def apply_robot_voice(data, rate):
    """Apply a robot-like voice effect."""
    mod_freq = 30  # Modulation frequency in Hz
    t = np.arange(len(data)) / rate
    mod_signal = np.sin(2 * np.pi * mod_freq * t)
    return np.clip(data * mod_signal, -1.0, 1.0)

def apply_voice_removal(data):
    """Remove vocals by filtering the center channel."""
    if data.ndim == 2:
        return (data[:, 0] - data[:, 1]) / 2
    else:
        print("Warning: Voice removal requires a stereo file. Converting mono to stereo for processing.")
        stereo_data = np.column_stack((data, data))
        return (stereo_data[:, 0] - stereo_data[:, 1]) / 2

def main():
    parser = argparse.ArgumentParser(description="Audio Effects Processor")
    parser.add_argument("input_file", help="Path to the input WAV file")
    parser.add_argument("output_file", help="Path to save the output WAV file")
    parser.add_argument("--volume", type=float, default=1.0, help="Volume adjustment factor (default: 1.0)")
    parser.add_argument("--bass", type=float, default=0.0, help="Bass boost factor (default: 0.0)")
    parser.add_argument("--delay", type=float, nargs=2, metavar=("DELAY_SEC", "DECAY_FACTOR"), help="Apply delay effect (seconds, decay factor)")
    parser.add_argument("--reverb", type=float, default=0.0, help="Apply reverb effect (reverb decay seconds)")
    parser.add_argument("--robot", action="store_true", help="Apply a robot voice effect")
    parser.add_argument("--remove-voice", action="store_true", help="Remove vocals from a stereo track")
    args = parser.parse_args()

    # Read the WAV file
    try:
        data, rate = sf.read(args.input_file)
    except Exception as e:
        print(f"Error: Unable to read the file '{args.input_file}'. Ensure it's a valid WAV file.")
        print(f"Details: {e}")
        return

    # Normalize data
    data = data / np.max(np.abs(data)) if np.max(np.abs(data)) != 0 else data

    # Apply effects
    if args.volume != 1.0:
        data = apply_volume(data, args.volume)
    if args.bass > 0.0:
        data = apply_bass(data, args.bass)
    if args.delay:
        delay_sec, decay_factor = args.delay
        data = apply_delay(data, rate, delay_sec, decay_factor)
    if args.reverb > 0.0:
        data = apply_reverb(data, rate, args.reverb)
    if args.robot:
        data = apply_robot_voice(data, rate)
    if args.remove_voice:
        data = apply_voice_removal(data)

    # Save the output
    try:
        sf.write(args.output_file, data, rate)
        print(f"Processed file saved to {args.output_file}")
    except Exception as e:
        print(f"Error: Unable to save the output file '{args.output_file}'.")
        print(f"Details: {e}")
        return

    # Play the processed audio
    try:
        print("Playing the processed audio...")
        sd.play(data, samplerate=rate)
        sd.wait()
    except Exception as e:
        print(f"Error: Unable to play the audio. Details: {e}")

if __name__ == "__main__":
    main()
