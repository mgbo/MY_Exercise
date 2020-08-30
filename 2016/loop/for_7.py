"""
def gcd(a, b):
    Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    
    while b:
        a, b = (b, a%b)
    return a
    
(a,b)=map(int,raw_input().split())
ans=gcd(a,b)
print "GCD= %d"%ans
"""



def sol(a,b):
	while a!=b:
	 if a>b:
	  a=a-b
	 else:
	  b=b-a
	return a

(a,b)=map(int,input().split())

gcd=sol(a,b)
gcf=a*b/gcd

print (("%d %d")% (gcd,gcf))









