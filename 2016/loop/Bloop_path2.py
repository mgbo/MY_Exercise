# -*- coding: utf-8 -*-

(l,k)=map(int,raw_input().split())

i=0
step=0
path=0

while i<7:
	path=path+step
	print "path = %d" % path
	
	i=i+1
	print "количество шагов =%d"% i
	
	step=step+k
	print "step = %d" % step
	
	
	
print path
