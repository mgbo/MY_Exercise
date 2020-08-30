
from sympy import*

x=symbols('x')

ans=integrate(6*x**5,x)
print ans

ans1=integrate(sin(x),x)
print ans1

ans2=diff(sin(2*x),x)
print ans2

pprint(Integral(x**2,x))

pprint(diff(x**3,x))

'''
from sympy import*


#sys.displayhook = pprint

var("x")


pprint(Integral(x**2,x))

pprint(x**3/3)
'''