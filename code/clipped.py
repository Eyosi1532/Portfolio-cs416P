#Eyosi Desta
#Clipped assignment

import numpy as np
import scipy.io.wavfile as wavfile
import sounddevice as sd

#define variables 
Amplitude = 8192
Duration = 1
Frequency = 440
Sample_rate = 48000

Max_threshold = 8192 #max amplitude threshold for clipping
Max_clipped = 16384 #max amplitude for the clipped sine wave 

#function to generate a sine wave
def generate_sine (frequency, sample_rate, duration, amplitude):
    t = np.linspace(0,duration,int(sample_rate * duration), endpoint= False)
    sine_wave = amplitude * np.sin(2*np.pi * frequency * t)
    return sine_wave.astype(np.int16) #change to 16-bit signed integers

#function to generate a clipped sine wave
def generate_clipped (frequency , sample_rate, duration, amplitude, max_threshold):
    sine_wave = generate_sine(frequency,sample_rate,duration,amplitude)
    sine_wave[sine_wave > max_threshold] = max_threshold #clipping positive values 
    sine_wave[sine_wave < -max_threshold] = -max_threshold #clipping negative values
    return sine_wave

#save the generated sine wave to a WAV file
def write_wav (filename, sample_rate, data):
    wavfile.write(filename, sample_rate, data)

#play the audio using sounddevice
def play_audio(data, sample_rate):
    sd.play(data,sample_rate)
    sd.wait() 

if __name__ == "__main__":
    sine_wave = generate_sine(Frequency, Sample_rate, Duration, Amplitude)
    write_wav("sine.wav", Sample_rate, sine_wave)
    print("sine.wav is generated")

    clipped_sine = generate_clipped(Frequency, Sample_rate, Duration, Max_clipped, Max_threshold)
    write_wav("clipped.wav", Sample_rate, clipped_sine)
    print("clipped.wav is generated")

    print(" Playing ... ") 
    play_audio(clipped_sine, Sample_rate)
