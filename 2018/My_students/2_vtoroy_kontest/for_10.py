
'''
d,n = map(int,input().split())

count = 0
nn = 0
while n>0:
	osta = n%10
	#print (osta)
	if osta==d:
		count+=1
	n=n//10
'''
n = input()

nn = len(n)
print (nn)


for i in range(nn):
	osta = int(n)%10
	ans *= osta*10
	print (ans)
	n =int(n)/10


print (ans)
