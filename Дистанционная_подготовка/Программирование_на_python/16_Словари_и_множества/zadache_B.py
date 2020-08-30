
f = list(map(int,input().split()))
s = list(map(int,input().split()))

count = 0

for i in f:
	for j in s:
		if i==j:
			#print (i,j)
			count+=1

print (count)