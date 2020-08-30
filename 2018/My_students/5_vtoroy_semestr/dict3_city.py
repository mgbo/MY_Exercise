
n = int(input())

d = {}

for i in range(n):
	infor = list(map(str,input().split()))
	key = infor[0]
	value = infor[1:]
	for v in value:
		if v not in d:
			d[v] = [key]
		else:
			d[v].append(key)

n = int(input())
for j in range(n):
	city = input()

	for k,v in d.items():
		if city==k:
			print (city,*v)


	
