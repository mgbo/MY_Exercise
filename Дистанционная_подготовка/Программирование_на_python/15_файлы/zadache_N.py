
d = {}


with open('file_N.txt', 'r') as f:
	for i in f:
		s_i = i.split()
		#print (s_i)

		klass = s_i[2]
		mark = int(s_i[3])

		if klass in d:
			d[klass].append(mark)

		else:
			d[klass]= []
			d[klass].append(mark)

for k,v in d.items():
	print ("class {} --> list : {}".format(k,v))
f.close()





