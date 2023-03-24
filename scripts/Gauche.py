import numpy as np 
import matplotlib.pyplot as plt

# f = plt.figure()
# f.set_figwidth(10)
# f.set_figheight()


t = np.arange(0,2,2/2000)
xx = 5
xy = 3
yy = 1
Map = [[xx,xy,xy],
	   [yy,yy,xy],
	   [yy,xy,yy]]
shift =[np.cos(np.pi * t +np.pi/3*2*i) for i in range(3)] 


# for i in range(len(shift)):
# 	for j in range(len(shift[i])):
# 		if shift[i][j] < 0:
# 			shift[i][j] = 0

total = 0 * t
# for i in Map:
# 	# total = 0 * t	
# 	for j , k in enumerate(i):
# 		# print(k)
# 		cach = k * shift[j]
# 		plt.plot(t*180 , cach)
# 		# total += cach
for j , k in enumerate(Map[2]):
	# print(k)
	cach = k * shift[j]
	plt.plot(t*180 , cach)
	total += cach

plt.plot(t*180 , total)

plt.xlim(0,360)

plt.show()