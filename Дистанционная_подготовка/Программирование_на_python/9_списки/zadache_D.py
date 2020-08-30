
l = list(map(int,input().split()))

a = l[0]

for i in range(len(l)-1):
	if a < l[i+1]:
		print (l[i+1], end=' ')
	a = l[i+1]
print ()

#print (*l_num)
