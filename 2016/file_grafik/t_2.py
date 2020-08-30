
# -*- coding:utf-8 -*-
lis_name = []

with open('tr.log','r') as f:
	for line in f:
		s = line.split()
		nazvaniye = s[2]
		lis_name.append(nazvaniye)
f.close()

raznyye_name = set(lis_name)
for i in raznyye_name:
	print (i)

print ("\n----------\n")

D = {}
for j in lis_name:
	D[j] = D.get(j,0)+1

for k,v in D.items():
	print(k,v)


