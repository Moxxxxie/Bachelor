import matplotlib.pyplot as plt
import numpy as np
import sys

# a = '''0.0000   0.00000000      0.00000000
# 0.1425   0.30426728      0.00121348
# 0.2856   0.60978345      0.00379067
# 0.4289   0.91560026     -0.00128846
# 0.5715   1.21995153     -0.01909337
# 0.7147   1.52568839     -0.04669514
# 0.8577   1.83089182     -0.06703489
# 1.0000   2.13475569     -0.03702585'''


pplot = []

def Getplot(x):
	with open(x) as f:
		flag = False
		x = []
		y = []
		for i in f.readlines():
			if i == '\n' or not(i) :
				flag = False
				continue
			else:
				if 'Interp' in i:
					flag = True
					continue
				if flag:
					c = i.replace('\n' , '')
					c = c.split()
					# print(c)
					# input()
					x.append(float(c[1]))
					y.append(float(c[2]))
				else:
					if len(x) > 0:
						pplot.append([x,y])
						flag
						x = []
						y = []
	# print("Extraction complete!")					







if len(sys.argv) > 1:
	Getplot(sys.argv[1])
	if len(sys.argv)  == 4:
		b = int(sys.argv[2])
		e = int(sys.argv[3])
	else:
		b = 0 
		e = len(pplot)


	for i in range(b,e):
		plt.plot(pplot[i][0],pplot[i][1],'b-')
	# plt.plot(pplot[14][0],pplot[14	][1] , 'r.-')
	


	# plt.xticks(pplot[b][0][::5])
	# plt.yticks(pplot[b][1][::5])
	plt.show()
else:
	print('Usage Neb_snap.py NEB_INTERP_file.interp First_iter(default 0) Last_iter(default -1 - last one)')






# b  = a.split('\n')
# X=[]
# Y=[]
# for i in b:
# 	c , x , y = i.split()
# 	X.append(float(x))
# 	Y.append(float(y))

# plt.plot(X,Y,'*-')
# # cc = list(np.arange(X[0],X[-1],len(X)))
# # print(cc
