import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd

# Constants
SAMPLE_RATE = 44100  # Standard sample rate (Hz)
DURATION = 0.5  # Duration of each note (seconds)

# Frequencies for the C major scale (C, D, E, F, G, A, B, C)
# Frequencies based on the 12-tone equal temperament system
C_MAJOR_SCALE_FREQUENCIES = {
    'C': 261.63,  # C4
    'D': 293.66,  # D4
    'E': 329.63,  # E4
    'F': 349.23,  # F4
    'G': 392.00,  # G4
    'A': 440.00,  # A4
    'B': 493.88,  # B4
    'C_high': 523.25  # C5
}

# Function to generate a sine wave for a given frequency
def generate_sine_wave(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * frequency * t)

# Generate the full C major scale as a list of sine waves
def generate_c_major_scale():
    scale_wave = []
    for note in C_MAJOR_SCALE_FREQUENCIES.values():
        wave = generate_sine_wave(note, DURATION, SAMPLE_RATE)
        scale_wave.append(wave)
    return np.concatenate(scale_wave)

# Save the scale to a WAV file
def save_to_wav(filename, data, sample_rate):
    wav.write(filename, sample_rate, data)

# Play the scale using sounddevice
def play_sound(data, sample_rate):
    sd.play(data, sample_rate)
    sd.wait()  # Wait until the sound finishes playing

# Main function to generate, save, and play the C major scale
def main():
    # Generate the C major scale
    scale = generate_c_major_scale()
    
    # Normalize the wave to fit in the 16-bit audio format (-32768 to 32767)
    scale = np.int16(scale / np.max(np.abs(scale)) * 32767)
    
    # Save the scale as a WAV file
    save_to_wav("c_major_scale.wav", scale, SAMPLE_RATE)
    
    # Play the scale
    play_sound(scale, SAMPLE_RATE)

    print("C Major Scale has been saved as 'c_major_scale.wav' and is now playing.")

if __name__ == "__main__":
    main()
