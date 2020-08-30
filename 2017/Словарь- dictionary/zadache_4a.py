
# -*- coding:utf-8 -*-
A = dict()

f = open('list_coun.txt','r')

for line in f:  
	F = line.split()
	print ("F is : ",F)
	if not F:
		break
	key = F[0]
	#del F[0]
	val = F[1:]
	A[key] = val
    
f.close()

for k,v in A.items():
	print (k,v)














