
# -*- coding: utf-8 -*-

import sys
b = []
for a in sys.stdin:
	x = list(map(int,a.split()))
	print ('x :',x)
	b = b + x
	print ('b : ',b)

print (" x : ",b)
sl=set(b)
print('----')
print (sl)


for n in sorted(sl):
	p=b.count(n)
	print (n,p)
