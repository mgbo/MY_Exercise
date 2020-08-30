
a = map(int,input().split())


max_n = 0
for x in a:
	if max_n<=x:
		max_n=x

print (max_n)