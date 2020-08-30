
# -*- coding:utf-8 -*-
lis_name = []
lis_duration = []

with open('tr.log','r') as f:
	for line in f:
		s = line.split()
		dlitelna = s[3]
		lis_duration.append(dlitelna)
		nazvaniye = s[2]
		lis_name.append(nazvaniye)
f.close()

DD = {}
for j in lis_name:
	DD[j] = DD.get(j,0)+1

for k,v in DD.items():
	print(k,v)

print ("------------")

D = {name: ti for ti,name in zip(lis_name,lis_duration)}
print (D)

N_dlitelna = []
NN = []

N = input('Write of name of action :')
for k in D:
	if N in D[k]:
		N_dlitelna.append(k)

print ("------------")
print (N_dlitelna)

N_dlitelna = [float(i) for i in N_dlitelna]
print (sorted(N_dlitelna))








