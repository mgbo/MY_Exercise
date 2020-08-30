
# -*- coding:utf-8 -*-

n = [1,5,17,-22,4,4,4]
a ={}

for i in n:
	a[i] = a.get(i,0) + 1
	#print (" get ", a[i])

print ("\n----------\n")
for k,v in a.items():
	print (k,v)


