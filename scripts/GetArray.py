from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cmath as cc


def get_array(Path):
	img = Image.open(Path)
	x = []
	y = []
	x_ ,y_ = img.size
	ax_x = int(x_/2)
	ax_y = int(y_/2)
	for i in range(x_):
		for j in range(y_):
			flag = img.getpixel((i,j))
			if flag == 1 :
				x.append(((i)/ax_x))
				y.append((-1*(j)/ax_y))
				break
	return (img , x,y)

def get_amp_phase(x,y, frequency):
	N = len(x)
	F = []
	for k in range(frequency):
		F.append(0)
		for n in range(N):
			beta = 2*np.pi * n * k / N
			F[k] += y[n] * (np.cos(beta) +1j*np.sin(beta))
	A = list(map(lambda x: abs(x)/N, F))
	ph = list(map(lambda x : cc.phase(x) , F))
	return (A , ph)


# frequency = 10
# img , x , y = get_array('test.png')
# A , ph = get_amp_phase(x,y , frequency)
# FF = [i+1 for i in range(frequency)]
# plt.bar(FF, A)
# plt.show()



