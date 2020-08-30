
l = list(map(int,input().split()))

max_num = 0
for i in range(len(l)):
	if max_num<l[i]:
		max_num = l[i]
		ind = i

print (max_num,ind)