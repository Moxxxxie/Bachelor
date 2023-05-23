import numpy as np
import matplotlib.pyplot as plt
import random

randi = [0.800, 0.801, 0.752, 0.661, 0.169, 0.956, 0.949, 0.003, 0.201, 0.291, 0.615, 0.131, 0.241, 0.685, 0.116, 0.241, 0.849]
maxT = 40
t = 2
N = 7	
repeatition = 1
k1=0.2
k2=0.2

Seq = np.arange(0,maxT,	t)
MAA = [0 for i in range(len(Seq))]
MBB = [0 for i in range(len(Seq))]
for i  in range(repeatition):
	AA = list()
	BB = list()
	A = 4 
	B = 3
	flag = 0
	for s in Seq:
		for v in range(N):
			if randi[flag] < (A/N) :
				flag +=1
				print('A: ', flag)
				if randi[flag] < k1*t:
					flag += 1
					A-=1
					B+=1
					# BB.append(B)
					# AA.append(A)
			else:
				flag+=1
				print('B:',flag)
				if randi[flag] < k2*t:
					flag+=1
					A+=1
					B-=1
		print('B at ',t,' second: ',B)
		input()					


