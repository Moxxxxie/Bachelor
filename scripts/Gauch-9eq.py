import matplotlib.pyplot as plt
import numpy as np


figure , axis = plt.subplots(9 , 1)
t = np.arange(0,2,1/2000)

xx = 5
xy = 4
yy = 3

shift = [np.cos(np.pi*t + i*np.pi*2/3) for i in range(3)]

for i in range(9):
	axis[i].plot(t*180 , shift[i%3])

plt.show()