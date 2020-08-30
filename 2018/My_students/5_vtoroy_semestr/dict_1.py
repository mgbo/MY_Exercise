
n = list(map(int, input().split()))

d = {}

for i in n:
	if i not in d:
		d[i]=d.get(i,1)
	else:
		d[i]+=1

for k,v in sorted(d.items()):
	print (k,v)


