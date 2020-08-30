
import sys

d = {}

for n in sys.stdin:
	i = n.strip()
	d[i] = d.get(i,0)+1

for k,v in d.items():
	print (k,v)