
n = int(input())

list_p = []
for i in range(n):
	x1,x2 = map(int,input().split())
	if x1<x2:
		list_p.append((x1,x2))

count = 0
for p in list_p:
	x1,x2 = p
	if x2<=0:
		count +=1

print (count)