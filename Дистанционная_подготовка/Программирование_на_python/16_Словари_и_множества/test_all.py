
d = {}
while True:
	try:
		l = input()
		print ("l--->",l)
		key, value = l.split()
		print (key,value)
		if key in d:
			d[key].append(value)
		else:
			d[key]=[value]

	except EOFError:
		print ("Error EOF or empty input")
		l == ""
		break

for k,v in d.items():
	print (k,v)