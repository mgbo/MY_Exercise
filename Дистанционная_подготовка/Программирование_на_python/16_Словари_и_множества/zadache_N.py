
d = dict()

st = input().split()

print (st)

for s in st:
	if s in d:
		d[s] +=1
	else:
		d[s] = 1

print (d.items())

for i in d.items():
	#print (i[0]) # i[0] - это ключи словари
	# i[1] - это значение словари

	if i[1] == max(d.values()):
		print (i[0])
		break
