import matplotlib.pyplot as plt
import numpy as np
import sys

X = []
Y = []
Z = []
temp = []
flag = False

def get_file(x):
	global X ,Y ,Z,temp
	with open (x) as f:
		for val in f.readlines():
			if val :
				S = val.replace('\n','')
				S = S.split()
				if not(float(S[0]) in X) :
					X.append(float(S[0]))
					if len(X) > 1:
						Z.append(temp)
						temp=[]
				if not(float(S[1]) in Y):
					Y.append(float(S[1]))
				temp.append(float(S[2]))
		Z.append(temp)


if len(sys.argv) < 1 :
	print('Usage : Surface.py file_name.txt')
else:
	get_file(sys.argv[1])
	# print(len(X) , len(Y))
	x, y  = np.meshgrid(X,Y)
	fig = plt.figure()
	Z = np.array(Z)
	ax = fig.add_subplot(1,1,1, projection='3d')
	ax.plot_surface(x,y,Z,cmap='plasma')
plt.show()