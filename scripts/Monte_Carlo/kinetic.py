import numpy as np
import matplotlib.pyplot as plt
import random


maxT = 10
t = 0.02
N = 100	
repeatition = 10
k1=0.4
k2=0.5

Seq = np.arange(0,maxT,	t)
MAA = [0 for i in range(len(Seq))]
MBB = [0 for i in range(len(Seq))]
for i  in range(repeatition):
	AA = list()
	BB = list()
	A = 0.8 * N
	B = 0.2 * N
	for s in Seq:
		for v in range(100):
			if random.random() < (A/N) :
				if random.random() < k1*t:
					A-=1
					B+=1
			else:
				if random.random() < k2*t:
					A+=1
					B-=1

		BB.append(B)
		AA.append(A)
	# plt.plot(Seq,AA)
	# plt.plot(Seq,BB)
	
	for j in range(len(Seq)):
		MAA[j] = MAA[j] + AA[j]
		MBB[j] = MBB[j] + BB[j]

MAA = list(map(lambda x : x / repeatition , MAA))
MBB = list(map(lambda x : x / repeatition , MBB))


plt.plot(Seq,MAA)
plt.plot(Seq,MBB)
plt.show()


