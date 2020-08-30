
import sys
d ={}

for s in sys.stdin:
	imya, *veshchi = s.split()
	#print (imya,veshchi)
	if imya not in d:
		d[imya] = [veshchi]
	else:
		d[imya].append(veshchi)

print (d)

value = {}

for k,v in sorted(d.items()):
	print (str(k) + " : ")
	kolichectbo = int(v[0][1])
	d_new = {}

	for vv in v:
		d_new[v[0]]=v[1]
		