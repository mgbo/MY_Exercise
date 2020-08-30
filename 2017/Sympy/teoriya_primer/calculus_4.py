
from sympy import integrate, exp, sin, log, oo, symbols

x,y = symbols('x,y')

ans = integrate(6*x**5,x)

print (ans)
