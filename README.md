# Portfolio-cs416P

Welcome to my CS416 portfolio for Computers, Sound And Music Fall term cource. This repository contains a collection of my work and activity throughout the cource. 

# Repository collections 

# assignment 1: Clipped 

## Overview 
This project consists of Python program that generates a WAV files 

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



[Enginnering Notebook](notebook.md)
- this contains a dated diary entries of my work and progress 

[Code](code/)
- this contains all programming assignment codes 


