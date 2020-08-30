
import sys

b=[]

for line in sys.stdin:
	a = map (int, line.split())
	print a
	
	b=b+a
	print b
	
	print '----'
	
mina=min(b)
maxa=max(b)
print mina,maxa
