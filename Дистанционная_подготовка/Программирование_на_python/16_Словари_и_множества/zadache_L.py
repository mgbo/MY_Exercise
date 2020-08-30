
n = int(input())

d = dict(input().split() for j in range(n))

print (d.items())

s = input()

for k,v in d.items():
	if v == s:
		print (k)
	if k == s:
		print (v)
