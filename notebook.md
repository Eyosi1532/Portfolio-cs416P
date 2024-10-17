Engineering notebook

# week1 

## Sound Basics 

- Sound is pressure waves in air or other medimus. Speed in air: ~1000 ft/s, in water: ~5000 ft/s 
- Wavelength is related to speed(s) and frequency(f) 
	- speed = frequency x wavelength 


## Key Frequencies 

- 60 Hz: ~17 ft wavelength 
- 1 kHz: ~1 ft wavelength 
- 15 kHz: ~1 inch wavelength. 

## Amplitude 

- Two main types: 
	1. Peak-to-peak(PP): Difference between highest and lowest points in a cycle. 
	2. RMS: Power delived is proportional to RMS 

## Other Notes 

- Latency - Delay between sound production nd hearing. 
	  - Reverb uses delayed copies of a signal. 

- Any repeating sound is a sum of sine waves with different amplitudes, frequencies, and phases 

- Prolonged exposure to sounds above 85 dBA can cause hearing loss. It is important to use ear protection for sustained loud sounds. 

- Localization in space is based on time and level difference between ears, with phase used below 1 kHz and group delay above 1.3 kHz 

## Impulses, Noise, Vibration, Distortion, and Feedback 

- Impulse contains all audible frequencies. 
- Noise constains a mix of random frequencies
- Vibrations produce harmonics, multiples of a fundamental frequency. 
- Distortion is result from nonlinearity or history of the signal. 
- Feedback causes resonance in systems like microphone speaker loops. 

# week2 

## Discretization of Sound 

- Discretization involves converting continuous analog signals into digital samples over time and amplitude. 
- Uniform time sampling and fixed-size binary amplitude values are commonly used, forming the basic for Pulse Code Modulation (PCM), the primary method of digital audio representation. 

### Advantages of PCM 
- PCM is resilient to noise, as minor amplitude variations are ignored. 
- Digital formats allow for perfect storage and transmission since any loss occurs during the conversion process. 
- PCM can easily manipulated on computers, though audiophiles sometimes prefer analog for higher fidelity. 

## Sample Representation 

- Audio is represented as sequences of numbers, with typical sample rates for human hearing at 44,100 sps and lower rates for telephony at 8,000 sps. 
- 16-bit samples are standard, though lower bit depths can still produce intelligible audio with non-linear encoding 

- Audio samples can be stored as integers or floating point numbers. Floating point allows for greater precision, avoiding overflow issues during calculations. 
- Fied point representation, though less common, is used in specialized hardware and DSP chips. 

## Digital-to-Analog and Analog-to-Digital Conversion 

- DACs convert digital signals into analog voltages, with methods like R/2R Ladder being fast but prone to accuracy issues. 
- PWM is another technique for digital to analog conversion, although it's challenging to filter correctly for high quality audio

## Audio Frameworks 
- Audio frameworks vary across operating systems. Linux commonly uses ALSA for drivers and PulseAudio for system audio managment, while Jack is used for professional low-latency applications. 
- New developments, such as PipeWire, aim to integrate ALSA, PulseAudio, and Jack into a unified system. 

# week3

## fourier 
- Fourier's Theorem states that any periodic sound can be broken dowm into a sum of sine waves, and the human ear perceives sound in terms of there frequencies. 
- Sound, represented as a continuous waveform, can be converted into a frequency spectrum, where amplitude and phase are associated with each frequency. 

### Time Domain vs Frequency Domain 
- Time domain is described by f(t), the pressure variation over time 
- Frequency domain represented by f(w),a spectrum showing how much energy is present at each frequency  

## Discrete-Time Fourier Transoform 
- To make Fourier analysis more practical, we get rid of the infinite limits by considering signals over a finite period.
- The DTFT approximates the continous Fourier Transform by summing values over a finite time period. 

### Key points About the DFT 
- The frequency values are still complex numbers, containing both magnitude and phase information. 
- The inverse transorm is computed using a sum over discrete frequencies. 

## Notes 

- Sound synthesis refers to generating sound, often through mathematical models or electronic instruments, as opposed to analyzing pre-existing sounds. 
### Wavetables, Additive/Subtractive Synthesis, Frequency Modulation, Advanced Techniques
- Wavetables: pre-recorded waveforms used to generate sound. 
- Additive/Subtractive Synthesis: Adding or filtering frequencies to shape sound 
- Frequency Modulation: Varying one frequency with another to create complex tones. 
- Advanced Techniques: Various other methods, sometimes involving physical modeling or granular synthesis. 

### Note Timing 
- Notes not only have a pitch or grequency but also a start time and duration. The on-time marks when the note begins, and the off-time specifies when it ends. 
	- Start times are typically between 4-30ms apart. 
	- Durations start around 4ms and increase based on the musical context. 
	- Some instruments are monophonic, playing only one note at the time, while others allow polyphony, where multiple notes overlap. 


