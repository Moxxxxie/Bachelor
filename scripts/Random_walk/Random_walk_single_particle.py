import matplotlib.pyplot as plt
import numpy as np
import random



T = 100
t = 0.1
Seq = np.arange(0,T,t)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')



lastposition = [0. , 0.]
verts = [(0. , 0.)]
# moves = list(zip(x , y))
for i in range(len(Seq)):
	lastposition = [lastposition[0] + random.randint(-1,1) , lastposition[1]+random.randint(-1,1)]
	verts.append(tuple(lastposition))


x = [verts[i][0] for i in range(len(Seq))]
y = [verts[i][1] for i in range(len(Seq))]
# print(x,y)
maxy = max(y)+10
maxx = max(x)+10
a = 100
plt.xlim(-1*a,a)
plt.ylim(-1*a,a)

plt.plot(x,y,'black')

plt.plot(lastposition[0],lastposition[1],marker ='o',c='g')
plt.plot(0,0,marker ='o',c='r')
# plt.quiver(0,0 , lastposition[0],lastposition[1] , color = 'green',units='xy',scale= 1)
plt.show()