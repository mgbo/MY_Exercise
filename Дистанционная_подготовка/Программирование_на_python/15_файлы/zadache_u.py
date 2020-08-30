
d = {}

with open('file_U.txt') as f:
	for i in f:
		i_s = i.split()
		name = i_s[:2]
		full_name = ' '.join(name)
		#print (full_name)

		mark = i_s[-1]

		if full_name in d:
			d[full_name]=mark
		else:
			d[full_name]=mark


for k,v in sorted(d.items()):
	print (k,v)

f.close()
