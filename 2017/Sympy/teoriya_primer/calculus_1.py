
from sympy import*

x = Symbol("x")

ans = limit(sin(x)/x,x,0)
print (ans)

w = symbols('w')

eq = integrate(cos(w*x),x)
pprint (eq)

