import numpy as np
import matplotlib.pyplot as plt
import GetArray


plt.style.use('seaborn-poster')
# %matplotlib inline



# t = np.arange(0,1,1.0/2000)


# freq = 1.
# x = 3*np.sin(2*np.pi*freq*t)
# freq = 4
# x += np.sin(2*np.pi*freq*t)
# freq = 7   
# x += 0.5* np.sin(2*np.pi*freq*t)


# plt.figure(figsize = (8, 6))
# plt.plot(t, x, 'r')
# plt.ylabel('Amplitude')
# plt.show()
a , x ,y =  GetArray.get_array("test.png")
# print(y)
from numpy.fft import fft , ifft

X = fft(y)
N = len(X)
n = np.arange(N)
T = N/2000
freq = n / T


plt.stem(freq,np.abs(X),markerfmt=" ", basefmt="-b")
# plt.plot(x,ifft(X))
# plt.plot(x,y)
plt.xlim(0,10)
plt.show()
