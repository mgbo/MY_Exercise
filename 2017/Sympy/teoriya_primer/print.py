
from sympy import*
import numpy as np

x=symbols('x')

eq = exp(x)+5
pprint(eq)

ans=integrate(6*x**5,x)
print (ans)

ans1=integrate(sin(x),x)
pprint (ans1)

ans2=diff(sin(2*x),x)
pprint (ans2)

pprint(Integral(x**2,x))

pprint(diff(x**3,x))
print ('\n')

i = Integral(x*root(1-x,3),(x,1,9))
pprint (i)

u = symbols('u',positive=True)
iu = i.transform(1-x,u)

print ('\n')
pprint (iu)

ans1 = iu.doit()
pprint (ans1)


a,x0,sigma = symbols('a x0 sigma')

eq = a*exp(-(x-x0)**(2/(2*sigma**2)))
pprint (eq)


'''
from sympy import*


#sys.displayhook = pprint

var("x")


pprint(Integral(x**2,x))

pprint(x**3/3)
'''
