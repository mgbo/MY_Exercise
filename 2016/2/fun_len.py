from math import sqrt
 
def length(x1,y1,x2,y2):
	a=x1-x2;
	b=y1-y2;
	
	res=sqrt(a*a+b*b)
	return res
	
(x1,y1,x2,y2) = map(float,raw_input().split())
(a,b,c,d)=map(float,raw_input().split())

ans=length(x1,y1,x2,y2)
ans1=length(a,b,c,d)

print ans
print ans1


