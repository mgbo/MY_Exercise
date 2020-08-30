
from math import fabs

def len1(a,b):
	l=fabs(a-b)
	
	return l
	
(a,b)=map(float,raw_input().split())
	
ans=len1(a,b)
	
print ans
	
