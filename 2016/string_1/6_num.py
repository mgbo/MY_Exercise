
import sys
#a=map(int,raw_input().split())

b=[]

for line in sys.stdin:
	a=map(int,line.split())
	#b=b+a
	b.extend(a)
	
print a
print b
b.sort()
print b

