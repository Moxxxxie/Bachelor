import matplotlib.pyplot as plt
import numpy as np
import sys 


x = []
y = []
cc = []

def getplot(z):
	with open(z) as f:
		for i in f.readlines():
			c = i.replace('\n' , '')
			if c :
				c = c.split()
				x.append(float(c[0]))
				y.append(float(c[1]))
	v = z.replace('.dat' , '.stk')
	with open(v) as f:
		for i in f.readlines():
			c = i.replace('\n' , '')
			if c :
				c = c.split()
				cc.append(float(c[0]))
				# y.append(float(c[1]))
				


if len(sys.argv) > 1:
	getplot(sys.argv[1])
	# c = np.r_[True, y[1:] < y[:-1]] & np.r_[y[:-1] < y[1:], True]
	# print(c)
	plt.plot(x[::-1],y[::-1])
	plt.gca().invert_xaxis()
	# plt.xticks(cc)
	plt.show()
else:
	print("Usage IR.py IR_FILE.ir.dat")
