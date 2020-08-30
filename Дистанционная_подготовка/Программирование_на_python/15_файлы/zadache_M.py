
d = {}
cl  = []


with open('file_M.txt', 'r') as f:
	for i in f:
		s = i.split()

		klass = int(s[-2])
		cl.append(klass)

		ball = int(s[-1])

		if klass in d:
			d[klass] += ball
		else:
			d[klass] = ball

print ("kolichectbo : ",cl)
s = set(cl)
print (s)

for i in s:
	ans = cl.count(i)
	print ("class : {} ----> {} times".format(i,ans))
	
for k,v in d.items():
	print (k,v)


f.close()

