from sympy import symbols , Eq, solve ,cos , pi
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.ticker as ticker


x, y, z = symbols('x y z')
eq1 = Eq(x + y + z ,  5.9+z )
eq2 = Eq(x*(1+cos(pi*1*1/3))+y*(1+cos(pi*2*1/3))+z*(1+cos(pi*3*1/3)) , 0.9+z)
# eq4 = Eq(x*(1+cos(pi*1*4/3))+y*(1+cos(pi*2*4/3))+z*(1+cos(pi*3*4/3)) , 3.4+z)
eq3 = Eq(x*(1+cos(pi*1))+y*(1+cos(pi*2))+z*(1+cos(pi*3)) , z)
sol = solve((eq1,eq2,eq3),(x,y,z))
print(sol)

mp=[]

t = np.arange(0,2,1/1000)
# mp = [0.6,0,5.3]
for i in sol.keys():
	mp.append(float(sol[i]))
shift = [1+np.cos(np.pi*i*t) for i in range(1,4)]
shift[1] = -1 * shift[1]
for i in range(3):
	shift[i]=mp[i]*shift[i]
# print(type(mp[1]))

total = 0 * t
for i in shift:
	plt.plot(t*180,i)
	total += i

plt.plot(t*180,total)
# ax = plt.axes()
# ax.xaxis.set_major_locator(ticker.MultipleLocator(50))
# ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))
plt.xticks([i for i in range(0,361,30)])
plt.yticks([i for i in range(0,13,1)])
plt.show()	