


a = list(map(int, input().split()))
print ("сколько дано чисел : ", len(a))
print ("сколько числе без поврторов : ", len(set(a)))
d = {}

for x in a:
	d[x] = d.get(x, 0)
	if x in d:
		d[x]+=1

for k,v in sorted(d.items()):
	print (k,v)

