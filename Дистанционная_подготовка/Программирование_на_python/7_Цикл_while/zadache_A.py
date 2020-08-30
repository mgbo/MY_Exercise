
n = int(input())
ans=1
res=1

while res<=n:
	print (res,end=' ')
	ans+=1
	res=ans*ans
	
print()

"""
n = int(input())
 
l = [i*i for i in range(1,n) if i*i<=n]
 
print (*l)

"""
