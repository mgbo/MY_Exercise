
import sys

new = []
for l in sys.stdin:
	k, n = l.split()
	new.append([k,n])

def by_cls(kk):
	return int(kk[0]),kk[1]

for k,n in sorted(new, key=by_cls):
	print (k,n)
