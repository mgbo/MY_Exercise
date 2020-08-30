
f = open("input_F.txt",'r')

d = dict()

for w in f:
	l = w.split()
	#print (l)
	for ww in l:
		d[ww] = d.get(ww, 0) + 1

		print (d[ww] - 1,end=' ')

f.close()