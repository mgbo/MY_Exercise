
n = int(input())

list_p = []
for i in range(n):
	x1,x2 = map(int,input().split())
	if x1<x2:
		list_p.append((x1,x2))


l_x1, l_x2 = list_p[-1]

count = 0
for p in list_p[:-1]:
	x1, x2 = p
	if l_x1 <= x1 and l_x2 >= x2:
		count +=1

print (count)