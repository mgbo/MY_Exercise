
# -*- coding: utf-8 -*-


import sys

b=[]

for line in sys.stdin:
	a = map (int, line.split())
	print (a)
	
	b=b+a # так можно использовать только int типа
	print (b)
	
	print "----"

print (b)

mina=min(b)
maxa=max(b)
print mina,maxa
