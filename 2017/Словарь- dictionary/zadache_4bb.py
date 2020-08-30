
# -*- coding:utf-8 -*-

d = {}
f = open('list_coun.txt','r')

for line in f:  
	F = line.split()
	if not F:
		break
	state = F[0]
	for town in F[1:]:
 		d[town] = state
f.close()

for k,v in d.items():
    print(k,v)










