
d,n = map(int,input().split())

count = 0
nn = 0
while n>0:
	osta = n%10
	#print (osta)
	if osta==d:
		count+=1
	n=n//10


print (count)