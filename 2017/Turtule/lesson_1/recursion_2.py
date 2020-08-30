
n=int(input())

def fac(n):
  f=1
  x=2
  
  while x <= n:
   f*=x
   x+=1
   
  return f



print (fac(n))
