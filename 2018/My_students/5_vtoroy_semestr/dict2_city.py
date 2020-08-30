
n = int(input())

d = {}

for i in range(n):
	infor = list(map(str,input().split()))
	key = infor[0]
	value = infor[1:]

	d[key] = value

for i in range(n):
	city = input()
	for k,v in d.items():
		if city in v:
			print(key)

# for k,v in d.items():
# 	print (k,v)