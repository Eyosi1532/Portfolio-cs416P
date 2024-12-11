# Portfolio-cs416P

Welcome to my CS416 portfolio for Computers, Sound And Music Fall term cource. This repository contains a collection of my work and activity throughout the cource. 

# Repository collections 

# assignment 1: Clipped 

## Overview 
This project consists of Python program that generates a WAV files 

# Clipped assignment 
## Objectives 
1. **Generate and Save a Sine Wave**: 
- Create a 440 Hz sine wave and save it as 'sine.wav' with follwoing specifications: 
	- Mono channel 
	- 16-bit signed sample format 
	- 48,000 Hz sample rate 
	- Amplitude: 8192
2. **Generate and Save a Clipped Sine WAVE**: 
- Generate a clipped version of the sine wave where values exeeding (plus or munus 8192) are limited to those values. Save it as 'clipped.wav'

3. **Play the clipped Sine wave**: 
- Play the 'clipped.wav' file directly through the computer's audio output using the 'sounddevice' library. 

## Requirements 
- Python 3.9 or later
- Libraries: 'numpy', 'scipy', 'sounddevice' 

## How it works 

Run the script to generate the WAV files and play the clipped sine wave: 
'''bash 
python clipped.py
'''
## Sources:

- to generate the time points for the sine wave

https://stackoverflow.com/questions/61739446/using-numpy-linspace-method-for-a-simpleaudio-project-i-get-a-typeerror-when

- convert to 16-bit signed integers 
https://stackoverflow.com/questions/55474025/how-to-convert-int32-numpy-array-into-int16-numpy-array

https://docs.scipy.org/doc/scipy-1.13.1/reference/generated/scipy.io.wavfile.write.html


# FIR lowpas filter 
### FIR Lowpass Filter:
- A simple FIR lowpass filter implemented to process audio signals.  
- This project demonstrates the design and application of a basic FIR lowpass filter. The filter attenuates high-frequecy noise while allowing low-frequency components to pass through, showcasing the principles of FIR filtering in audio signal processing. 
### Requirments: 
-scipy
-soundevice 
-matplotlib
-replace clipped.wav with your own wave file. 

# C_major_scale.py
- This Python script generates and plays a C major scale using sine waves for each note. The scale is created based on the frequencies of the C major scale in the 12-tone equal temperament system. The program saves the scale as a WAV file and plays it using the `sounddevice` library.

### Requirements: 
- scipy
- sounddevice
- numpy

# Adaptive Tone Control
- This code provides a method for adjusting the energy in different frequency bands of an audio file. Using FFT, the audio is analyzed in the frequency domain, and enery levels in the low, mid, and high-frequency bands are equalized using bandpass filters. The resulting audio can be played back and saved to a new wave file. 

### Requirements: 
- scipy
- numpy
- sounddevice
- scipy.io.wavefile
# popgen
### Overview
- popgen generates a pop-style melody using the Axis Progression chord loop, complete with bass, rhythm, and melody lines. The program outputs a WAV file or plays audio directly.

### Features
  Customizable chord progressions, melody range, and rhythm.
- Supports sine, square, sawtooth, and triangle waveforms.
- ADSR envelope for smooth note transitions.
- Adjustable tempo, gain, and balance between melody and bass.

### key arguments
- --bpm
- --waveform
- --chord-loop
- --melody-range
- --output


# My Project 
# Audio Effects Processor

A Python-based command-line tool for applying various audio effects to WAV files, including volume adjustment, bass boost, delay, reverb, and robot voice effects. The program also supports voice removal from stereo tracks.

## Features

- **Volume Adjustment**: Amplify or reduce the audio volume.
- **Bass Boost**: Enhance low-frequency sounds for a deeper tone.
- **Delay Effect**: Add an echo-like delay to the audio.
- **Reverb Effect**: Simulate environmental reverberation, such as a hall or room.
- **Robot Voice**: Apply a robotic sound effect to the audio.
- **Voice Removal**: Remove vocals from stereo tracks by isolating the center-panned channel.

## Options and Flags 
- --volume <factor>
- --bass <factor>
- --delay <delay_sec><decay_factor>
- --reverb <reverb_decay>
- --robot
- --remove-voice


## Requirements

This program requires Python and the following Python libraries:

- `numpy`
- `soundfile`
- `sounddevice`
- `scipy`


```bash
pip install numpy soundfile sounddevice scipy

[Enginnering Notebook](notebook.md)
- this contains a dated diary entries of my work and progress 

[Code](code/)
- this contains all programming assignment codes 



