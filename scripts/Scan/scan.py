import os 
import sys
from subprocess import check_output
import argparse
import numpy as np
import itertools



KEY = '###'
parser = argparse.ArgumentParser()
parser.add_argument("--input", help="input file")
parser.add_argument("--range", help="range file")
args = parser.parse_args()

# Current_num = list()	

#FIND INDEX
def find(x):
	R = list()
	b = x.split(KEY)
	lenb=len(b)-1
	if len(b) > 1 :
		for i in range(lenb):
			k = len(b[i])
			for j in range(i):
				k = k +3 + len(b[j])- 1
			R.append(k)
		return R
	return -1




vrange = list()
inp = list()
vv = list()


#RANGE
if args.range:
	with open(args.range) as rng:
		for i in rng.readlines():
			f = list(map(float,i.replace('\n','').split(',')))
			vrange.append(list(map(lambda x : round(x , 6) , list(np.arange(f[0],f[1],(f[1]-f[0])/f[2])))))
else:
	print("No range file is specified")
	sys.exit()



#INPUT
if args.input:
	with open(args.input) as inpf:
		for i in inpf.readlines():
			inp.append(i)
			if KEY in i:
				c = find(i)
				for i in c:
					vv.append([len(inp)-1,i])
else:
	print("No input file is specified")
	sys.exit()



if len(vv) != len(vrange):
	print("Inputs does not match!")
	sys.exit()
flag = len(vrange[0])
Iter = len(vrange)
tick = [len(i) for i in vrange]
# for Subset  in itertools.combinations(vrange, len(vv)):
# 	print(Subset)
print(vv)
# bac = inp.copy()
# os.system('mkdir Scan')
# os.system('cd Scan')


parrent = args.input.replace('.inp', '')
try:
	os.mkdir(parrent)
except FileExistsError:
	pass
os.chdir(parrent)
for i in list(itertools.product(*vrange)):
	bac = inp.copy()
	for j in range(len(vv)):
		tag = vv[j]
		if len(inp[tag[0]]) == len(bac[tag[0]]):
			bac[tag[0]] = bac[tag[0]][:tag[1]] + ' ' 	+ str(i[j]) + ' ' + bac[tag[0]][tag[1]+len(KEY):]
		else:
			correction =  len(bac[tag[0]]) - len(inp[tag[0]])+1
			bac[tag[0]] = bac[tag[0]][:tag[1]+correction] + ' ' 	+ str(i[j]) + ' ' + bac[tag[0]][tag[1]+len(KEY)+correction:]

		# bac[vv[j][0]] = bac[vv[j][0]][:vv[j][1]] + ' ' + str(j) + ' '  bac[vv[j][0]][vv[j][1]+len(KEY)]
	dds = '_'.join(list(map(lambda x : str(x),i)))
	try:
		os.mkdir(dds)
	except:
		pass
	os.chdir(dds)
	f = open(dds+'.inp' , 'w')
	for cc in bac:
		f.write(cc)
	f.close()
	orca = '$HOME/CC/orca504s/orca ' + dds +'.inp > '+ dds + '.out'
	print(orca)
	os.system(orca)

	# print(''.join(bac))
	# os.system('echo ' + ''.join(bac) + ' > ' +dds+'.inp')
	# file = ' '.join(bac)
	# os.system('echo ' + file + ' > ' +dds+'.inp')
	os.chdir('..')





