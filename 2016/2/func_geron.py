from math import sqrt

def length(x1,y1,x2,y2):
	a=x1-x2
	b=y1-y2
	res=sqrt(a*a+b*b)
	return res

def mid(a,b,c):
	p=(a+b+c)/2
	return p

(x1,y1,x2,y2,x3,y3)=map(float,raw_input().split())

len1=length(x1,y1,x2,y2)
len2=length(x2,y2,x3,y3)
len3=length(x3,y3,x1,y1)

pp=mid(len1,len2,len3)

ans=sqrt(pp*(pp-len1)*(pp-len2)*(pp-len3))

print ans	

