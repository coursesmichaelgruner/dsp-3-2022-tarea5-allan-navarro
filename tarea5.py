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

plt.figure('prob2')
plt.plot(freq, fft.real,freq, fft.imag)
plt.legend(['Real','Imag'])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("DFT")


freq_split = freq[:len(freq)//2]
fft_split = fft[:len(fft)//2]

freq_split= freq_split[:len(fft)//24]
fft_split= fft_split[:len(fft)//24]

harmonics = np.arange(1,30)*60

plt.figure('prob3')
plt.plot(freq_split, np.abs(fft_split))
plt.vlines(harmonics,ymin=0,ymax=np.max(np.abs(fft_split)),linestyles='dotted',colors='red')
plt.legend(['DFT','armónicos'])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (DFT)")

plt.show()