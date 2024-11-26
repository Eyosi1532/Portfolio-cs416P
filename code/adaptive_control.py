import numpy as np
import scipy.io.wavfile as wav
from scipy.fft import fft, ifft
from scipy.signal import butter, lfilter
import sounddevice as sd

# Load the WAV file
sample_rate, audio_data = wav.read('sample.wav')

# Ensure the audio data is mono
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Apply FFT to get the frequency domain representation
N = len(audio_data)
freqs = np.fft.fftfreq(N, 1/sample_rate)
fft_data = fft(audio_data)

# Split the FFT into low, mid, and high bands
low_band = (freqs >= 0) & (freqs <= 300)
mid_band = (freqs > 300) & (freqs <= 2000)
high_band = (freqs > 2000)

# Compute the energy in each band
low_energy = np.sum(np.abs(fft_data[low_band])**2)
mid_energy = np.sum(np.abs(fft_data[mid_band])**2)
high_energy = np.sum(np.abs(fft_data[high_band])**2)

# Normalize the energies to balance them
total_energy = low_energy + mid_energy + high_energy
target_energy = total_energy / 3  # We want each band to have roughly equal energy

# Apply tone filters to adjust energy in each band (basic equalizer concept)
def bandpass_filter(data, low_cutoff, high_cutoff, sample_rate, order=6):
    nyquist = 0.5 * sample_rate
    if low_cutoff <= 0 or high_cutoff <= 0:
        raise ValueError("Filter cutoff frequencies must be greater than 0.")
    if low_cutoff >= nyquist or high_cutoff >= nyquist:
        raise ValueError(f"Filter cutoff frequencies must be less than the Nyquist frequency ({nyquist}).")
    if low_cutoff >= high_cutoff:
        raise ValueError("Low cutoff frequency must be less than high cutoff frequency.")
    
    low = low_cutoff / nyquist
    high = high_cutoff / nyquist
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)

# Apply the bandpass filter for low, mid, and high bands
filtered_audio = np.zeros_like(audio_data)

# Apply filter for low band (0-300 Hz)
filtered_audio[:len(audio_data)] = bandpass_filter(audio_data, 10, 300, sample_rate)

# Compute the adjustments needed for each band based on the energy
adjustment_factor = target_energy / np.array([low_energy, mid_energy, high_energy])

# Apply adjustments to the FFT data (scaling each band)
fft_data[low_band] *= np.sqrt(adjustment_factor[0])
fft_data[mid_band] *= np.sqrt(adjustment_factor[1])
fft_data[high_band] *= np.sqrt(adjustment_factor[2])

# Convert the adjusted FFT back to the time domain
adjusted_audio = np.real(ifft(fft_data))

# Convert back to integer data format for playback
adjusted_audio = np.int16(adjusted_audio)

# Play the modified audio
sd.play(adjusted_audio, sample_rate)
sd.wait()

# Optionally save the modified audio to a new file
wav.write('modified_audio.wav', sample_rate, adjusted_audio)
