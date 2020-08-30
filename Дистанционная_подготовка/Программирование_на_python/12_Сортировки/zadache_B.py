
l = list(map(int, input().split()))

for i in range(len(l)-1):
	if  l[i]<l[i+1]:
		ans = l[i+1]
		ind = i+1

print (ans,ind)
