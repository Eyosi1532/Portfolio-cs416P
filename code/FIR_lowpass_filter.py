import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import matplotlib.pyplot as plt

# Simple FIR Lowpass Filter: y[n] = 1/2 * (x[n] + x[n-1])
def fir_lowpass_filter(input_signal):
    output_signal = np.zeros_like(input_signal)
    
    # Apply the filter equation: y[n] = 1/2 * (x[n] + x[n-1])
    for n in range(1, len(input_signal)):
        output_signal[n] = 0.5 * (input_signal[n] + input_signal[n-1])
    
    return output_signal

# Load a WAV file
def load_wav_file(filename):
    sample_rate, data = wav.read(filename)
    print(f"Sample Rate: {sample_rate} Hz")
    print(f"Data Shape: {data.shape}")
    
    return sample_rate, data

# Save the processed WAV file
def save_wav_file(filename, sample_rate, data):
    wav.write(filename, sample_rate, data)

# Play the sound
def play_sound(data, sample_rate):
    sd.play(data, sample_rate)
    sd.wait()  # Wait until the sound has finished playing

# Main function
def main():
    # Load a WAV file
    sample_rate, data = load_wav_file('clipped.wav') 
    
    # Convert stereo to mono by averaging channels (if stereo)
    if len(data.shape) == 2:
        data = np.mean(data, axis=1)
    
    # Normalize to the range -1 to 1
    data = data / np.max(np.abs(data), axis=0)
    
    # Apply the FIR Lowpass filter
    filtered_data = fir_lowpass_filter(data)
    
    # Save the filtered result to a new WAV file
    save_wav_file('filtered_output.wav', sample_rate, filtered_data.astype(np.float32))
    
    # Plot original and filtered signals for comparison
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(data[:1000], label="Original Signal")
    plt.title("Original Signal")
    plt.subplot(2, 1, 2)
    plt.plot(filtered_data[:1000], label="Filtered Signal", color='r')
    plt.title("Filtered Signal")
    plt.tight_layout()
    plt.show()
    
    # Play the filtered sound
    play_sound(filtered_data, sample_rate)

if __name__ == "__main__":
    main()
