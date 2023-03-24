import numpy as np
import matplotlib.pyplot as plt

from scipy.fftpack import fft , ifft , fftfreq

plt.style.use('seaborn-poster')

t = np.arange(0,1,1.0/2000)
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)
freq = 4
x += np.sin(2*np.pi*freq*t)
freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)


X = fft(x)
# N = len(X)
# n = np.arange(N)
# T = N/2000
# freq = n / T
sig = X.copy()
# print(freq)
freq = fftfreq(len(X) , d =1./2000)
# print(freq)

cut_off = 6
sig[np.abs(freq) < cut_off] = 0
plot = ifft(sig)
plt.plot(t,plot)
plt.show()