#!/usr/bin/python3
import sys
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    print('please specify name of wav file')
    exit(1)

# Read wav file
fs, data = wavfile.read(sys.argv[1])
print(f'1. sample rate {fs}')

fft = np.fft.fft(data)

freq = np.fft.fftfreq(data.shape[-1])*fs

plt.figure(1)
plt.plot(freq, np.abs(fft))
plt.xlabel("Freqency (Hz)")
plt.ylabel("Magnitude")
plt.title("DFT")

plt.show()