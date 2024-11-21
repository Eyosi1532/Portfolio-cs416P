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


# week 4
## FIR filters Vs IIR filters 

### FIR filters 
- Impuls: Finite, as the output depends on a finite number of input samples.
- Stability: Always stable, since there is no feedback loop. 
- Design Flexibility: Easier to design with predictable frequency response characteristics 
- Implementation: Easier to implement in floating-point and fixed-point due to stability and lack of feedback 

### IIR filters 
- Impuls: Infinite, as it uses feedback, causing the response to continue indefinitely. 
- Stability: Potentially unstable if not designed carefully, due to feedback. 
Design Flexibility: More complex to design due to feedback; common to use standard methods
Implementation: Preferably implemented in floating-point due to potential for large or small intermediate values. 


#### conclusion: FIR filtes are easier to implement and stable, while IIR filters offer better performance per calculation. For many applications, Standard filter designs are available for both FIR and IIR, making it practical to look up designs rather than derive them manually.


## Resampling 

- In digital audio processin, resampling is the process of converting a single from one sample rate to another. This is essential for compatibility between systems and devices that operate at different rates. 

- Nyquist: if we change sample rates without addressing freqencies beyond the new Nyquist limit, we risk aliasing, causing distortion and unwanted frequencies in the output. 

### Resampling methods: 
#### 1. Low-Pass Filtering:
- To downsample, filter out frequencies above half of the target sample rate before taking fewe samples. 
- To upsample, insert zeros between sample and apply a low-pass filters to smooth the output signal. 

#### 2. Difital Filtering 
- Finite Impulse Response(FIR) filters can be used here, where the output is calculated using a weighted sum of previous samples with filter coefficients that act as a low-pass filter. 

## Expirment: FIR_lowpass_filter.py
- This week I implemented a python program called FIR_lowpass_filter.py
- Design and implement a simple FIR lowpass filter to process audio signals. The filter should reduce high-frequency noise while maintaining the integrity of low-frequency components.
#### Implementation:  
   - I used Python and the `scipy.io.wavfile` library to read and write WAV files.
   - I implemented the filter using a loop that applies the averaging formula to each sample.
   - I used the `sounddevice` library to play back the filtered audio and `matplotlib` to visualize the effects of the filter.
#### Results: 
   - The filter successfully reduced high-frequency noise, resulting in a smoother, less sharp audio signal.
   - I plotted the first 1000 samples of both the original and filtered signals for visual comparison, which showed a noticeable smoothing effect on the filtered signal.


# week5: Audio Effects and Processing 
## Overview of Audio Effects 
Audio effects modify an input sound to produce a different, often enhanced, version. These effects are widely used in commercial audio production to refine and improve sound quality or create artistic transformations. 
	- Read-Time Effects: Effects that operate on live audio must handle issues like low latency and simple hardware setups. 
	- Chains of Effects: Multiple effects are often applied in sequence, formating a Directed Acyclic Graph(DAG) for signal processing. 

## Types of Audio Effects
### 1. Compression and Expression: 
	- Compression: Reduces the dynamic range of the signal, making softer sounds louder and limiting louder sounds. Often used to maintain consistent volume levels. 
	- Expansion: Increases the dynamic range, making changes in volume more pronounced. 
### 2. Distortion and Noise Effects: 
	- Distortion: Alters the waveform by clipping or saturating the signal. Common examples include simulating tube amplifier distortion for "warmth."
	- Noise Addition: Adds modulated noise to a signal, such as white noise or frequency modulated noise. 
### 3. Delay Effects:
	- Small Delay: Creates phase cancellation and localization effects. 
	- Modderate Delays: Produces "ensemble" effects. 
	- Longer Delays: Generate reverb or echo effects by feeding back delayed signals. 
### 4. Reverb and Room Effects: 
	- Simulates the acoustic reflections and resonance of sound in a room. Delayed copies of the signal are filtered and fed back into the input for added realism. 

### 5. Modulation Effects: 
	- Vibrato: Oscillates the pitch of the sound. 
	- Tremolo: Oscillates the volume of the sound. 
	- Flanger: Mixes the original signal with a delayed version, creating phase cancellation patterns. 
	- Phaser: Similar to flanging but uses a series of all-pass filters to achieve the effect. 
	- Chorus: uses multiple delayes with varied times to simulate multiple voice or instruments playing the same melody. 

### 6. Resampling: 
	- Changing the sample rate of a signal, often for pitch shifting or time stretching. 
	- Pitch Shifting: Modifies the frequency of the signal without changing its duration. 
	- Time Stretching: Changes the length of the sound while preserving pitch. 

## Effects Plugins and Architecture
### Plugins: Modular pieces of software designed to be loaded into Digital Audio Workstations or other host environments to apply effects to audio. 
	- VST(Virtual Studio Technology): One of the most widely-used plugin formats, offering thousands of effects and instruments. 
	- LADSPA and LV2(Linux Audio Developer's Simple Plugin API): Popular in open-source and Linux audio environments, these plugin architectures provide a streamlined framework for adding audio effects to a system. 
	- JACK and Pipwire: Linux focused low-latency audio servers designed for professional grade audio processing, making them suitable for real-time performace or studio work. 

# week6

## Psychoacousics: Volume and Loudness 
### 1. Robinson-Dadson Curve(Fletcher-Munson Curve)
	- The Fletcher-Munson curve (also known as the Robinson-Dadson curve) illustrates the sensitivity of the human ear to different frequencies at various sound pressure levels. It shows how humans perceive volume, indicating that our ears are less sensitive to very low and very high frequencies at moderate loudness levels.
	- Three frequency bands were highlighted:
		-Below 100 Hz: Perception is less sensitive, with sound often felt rather than heard.
		- 100-400 Hz (Bass): Where the "bass" sounds lie.	
		- 400 Hz - 2 kHz (Midrange): Crucial for speech and many musical instruments.
		-2-10 kHz (Treble): Includes the brightness of sounds but less critical than midrange.
		- Above 10 kHz: Typically falls off in perceived loudness.
### 2. Volume Bands in Phon 
	- The human ear’s perception of volume is often measured in phon (dB relative to a 1 kHz tone).
		- 40 phon: Low, primarily affecting the midrange.
		- 50 phon: Normal, moderate midrange.
		- 70 phon: Loud, flat across frequencies.
		- 100+ phon: Aircraft-level volume, mostly affecting treble frequencies.

### Psychoacoustics: Harmonics, Stretch Tuning, Masking
	- Harmonics: Harmonics are multiples of the fundamental frequency and are important in the perception of timbre. For example, in a piano, the midrange harmonics of bass notes need to be stretch-tuned to sound in tune because the ear is more sensitive to midrange frequencies.
	- Masking: The ear’s selective hearing means that low-frequency sounds are often masked by higher-frequency sounds, especially in complex audio signals.

### Audio Compression

#### 1. Compression Models

	- Lossy Compression: Involves creating a simplified model of the audio signal, removing less critical data to reduce file size. Commonly used for MP3s and streaming services.
	- Lossless Compression: Uses the original signal with only small changes, keeping all details intact. FLAC is a good example of lossless compression.
#### 2. Types of Audio Compression
	- Time-Domain Models: Audio can be modeled using smooth curves, polynomials, or splines.
	- Frequency-Domain Models: Models the periodicity of audio signals by quantizing frequency and amplitude while ignoring phase.
#### 4.Residue: 
	- The difference between the original signal and the compressed model is called the residue, which is often perceived as noise. Compression schemes like Huffman coding exploit the distribution of this noise to further reduce file size.

### Compression Techniques
#### 1.Lossy Compression (e.g., MP3)

	- MP3 compression splits the audio signal into multiple frequency bands and then quantizes them to reduce file size. It uses Discrete Cosine Transform (DCT) and Huffman encoding to achieve compression.
	- MP3 Compression Steps:
		- Frequency splitting via polyphase filter.
		- FFT to analyze frequency content.
		- DCT to create a power spectrum.
		- Quantization and Huffman encoding of the spectrum.
#### 2.Lossless Compression (e.g., FLAC)

	- FLAC (Free Lossless Audio Codec) achieves compression by predicting audio content using polynomial models and encoding the difference (residue) using Rice codes.
	- FLAC compresses audio without any loss of quality, though it is not as efficient as lossy compression for some types of audio.

### Psychoacoustics and Practical Applications
#### Stereo Compression: 
- In stereo sound, left and right channels are highly correlated. By using techniques such as mono channels and side channels, stereo audio can be compressed efficiently without significant loss of quality.
#### Downsampling: 
- Since most audio signals contain minimal information at higher frequencies, downsampling reduces file size by preserving lower frequencies while discarding high-frequency information.

# week7

