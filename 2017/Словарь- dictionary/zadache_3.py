
# -*- coding: utf-8 -*-

#nob=[1,1,6,2,5,3,2,1,2,5,1,-1]
import sys
b = []
for a in sys.stdin:
	x = list(map(int,a.split()))
	b = b + x  

print (" x : ",b)
sl=set(b)
print ('----')
print (sl)

a={}

sset = sorted(set(b))
print ("sorted number",sset)

for n in sset[::-1]:
	#print "n : ",n
	p=b.count(n)
	a[n]=p
	print (n,p)
