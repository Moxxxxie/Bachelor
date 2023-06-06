import matplotlib.pyplot as plt
import numpy as np
import random

#Number of Particles
N = 100
#max time
T = 10
#time interval
t = 0.1
Seq = np.arange(0,T,t)

#Fig and plot settings
fig = plt.figure()
axs = [fig.add_subplot(220+i) for i in range(1,5)]
axs[0].spines['left'].set_position('center')
axs[0].spines['bottom'].set_position('center')
axs[0].spines['right'].set_color('none')
axs[0].spines['top'].set_color('none')
axs[0].xaxis.set_ticks_position('bottom')
axs[0].yaxis.set_ticks_position('left')

#dimension value for matrixes
a = 41
#to collect data to plot the bars
averx = {i:0 for i in range(-a+1,a,1) }
avery = {i:0 for i in range(-a+1,a,1) }
verts = [(0. , 0.)]

#get the last location
for j in range(N):
	lastposition = [0. , 0.]
	for i in range(len(Seq)):
		lastposition = [lastposition[0] + random.randint(-1,1) , lastposition[1]+random.randint(-1,1)]
	axs[0].plot(lastposition[0],lastposition[1],marker ='o',c='g')
	# dist = np.sqrt(lastposition[0]**2+lastposition[1]**2)
	averx[int(lastposition[0])] += 1
	avery[int(lastposition[1])] += 1

#plot settings
axs[0].title.set_text("Random Walk")
axs[2].title.set_text("X value")
axs[3].title.set_text("Y value")
#plot xvalue and yvalue of the particles
axs[2].bar(averx.keys(),averx.values())
axs[3].bar(avery.keys(),avery.values())

#ploting the contour map
xlist = [i for i in range(-a+1,a,1)]
ylist = [i for i in range(-a+1,a,1)]
X, Y = np.meshgrid(xlist, ylist)
x = np.array(list(avery.values())).reshape(1,-1)
y = np.array(list(averx.values())).reshape(-1,1)
Z = np.matmul(y ,x)
cp = axs[1].contourf(X,Y,Z)
fig.colorbar(cp , ax = axs[1])

plt.show()