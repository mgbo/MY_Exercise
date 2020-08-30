

d = {}
s = set()

with open('file_L.txt', 'r') as f:
	for i in f:
		s = i.split()

		klass = int(s[-2])
		ball = int(s[-1])


		if klass in d:
			if d[klass]<ball:
				d[klass] = ball
		else:
			d[klass] = ball


for k,v in d.items():
	print (k,v)


f.close()

