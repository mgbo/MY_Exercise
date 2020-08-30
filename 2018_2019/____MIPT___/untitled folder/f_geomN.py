
n = int(input())

list_p = []
for i in range(n):
	x1,x2 = map(int,input().split())
	if x1<x2:
		list_p.append((x1,x2))

max_length = 0
for p in list_p:
	x1,x2 = p
	length = abs(x2-x1)
	if max_length< length:
		max_length = length
		x,y = x1,x2

print (x,y)

