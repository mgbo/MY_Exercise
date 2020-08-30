
import sys

fp = sys.stdin

l = []
for s in fp:
	l.append(s.split())
	print (l)

print("print : ",l[1][4])