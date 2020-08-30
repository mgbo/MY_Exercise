
(d,n)=map(int,raw_input().split())
	
i=0

while n>0:
	if d==n%10:
		i+=1
	n=n/10
 

print i
