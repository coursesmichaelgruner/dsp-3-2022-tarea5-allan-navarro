#!/usr/bin/python3
import sys
from scipy.io import wavfile
import scipy.signal
from scipy.signal import lfilter
import numpy as np
import matplotlib.pyplot as plt
from math import cos, pi

if len(sys.argv) != 2:
    print('please specify name of wav file')
    exit(1)

# Read wav file
fs, data = wavfile.read(sys.argv[1])
print(f'1. sample rate {fs}')

fft = np.fft.fft(data)

freq = np.fft.fftfreq(data.shape[-1])*fs

plt.figure('prob2')
plt.plot(freq, fft.real, freq, fft.imag)
plt.legend(['Real', 'Imag'])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("DFT")


freq_split = freq[:len(freq)//2]
fft_split = fft[:len(fft)//2]

freq_split = freq_split[:len(fft)//24]
fft_split = fft_split[:len(fft)//24]

harmonics = np.arange(1, 30)*60

plt.figure('prob3')
plt.plot(freq_split, np.abs(fft_split))
plt.vlines(harmonics, ymin=0, ymax=np.max(
    np.abs(fft_split)), linestyles='dotted', colors='red')
plt.legend(['DFT', 'armónicos'])
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Magnitud (DFT)")

# fig, ax = plt.subplots(nrows=2, ncols=2)

# for i in range(1):
#     f,t,Zxx = scipy.signal.stft(data,fs,nperseg=256)

#     # fft_split = stft[:len(stft)//2]

#     # freq_split = freq_split[:len(fft)//24]
#     # fft_split = fft_split[:len(fft)//24]

#     ax[i//2, i % 2].pcolormesh(t,f,np.abs(Zxx),vmin=0,vmax=np.max(data), shading='gouraud')
#     ax[i//2, i % 2].set_ylim([f[1], f[-1]])
#     ax[i//2, i % 2].set_yscale('log')

#     # ax[i//2, i % 2].vlines(harmonics, ymin=0, ymax=10,
#     #                        linestyles='dotted', colors='red')

# fig.canvas.manager.set_window_title('prob4')

# fig.tight_layout()

def get_qs(f0):
    w0 = 2*pi*f0/fs
    r=0.999
    b=[1,-2*cos(w0),1]
    a=[1,-2*r*cos(w0),r*r]
    return b,a


plt.figure('notch')

res=data
for h in np.arange(1,10)*60:
    coeffs=get_qs(h)
    res=lfilter(coeffs[0],coeffs[1],res)
    w,a = scipy.signal.freqz(coeffs[0],coeffs[1],worN=1024,fs=fs)
    plt.plot(w,np.abs(a))

res = res.astype(np.int16)

wavfile.write("result.wav",fs,res)


plt.show()
