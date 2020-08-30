
import sys

f=open(sys.argv[1],'r')
t_prv=0

for line in f:
	print line
	
	a=map(int,line.split())
	print a
	
	t=a[0]
	d=a[1]
	id=a[2]
	print t
	print '_____'
	
f.close()
