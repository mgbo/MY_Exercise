
# -*- coding:utf-8 -*-
import sys

A = dict()

f = open('list_coun.txt','r')

for line in f:  
	F = line.split()
	print ("F is : ",F)
	if not F:
		break
	key = F[0]
	del F[0]
	val = F[1:]
	A[key] = val

print ("\n-----------------\n")


d = {}
for state,s in A.items():
	for town in s:
		d[town] = state

#print(d)

for s,v in d.items():
    print (s,v)
f.close()











