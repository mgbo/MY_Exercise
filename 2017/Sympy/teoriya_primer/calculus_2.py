
from sympy import diff, Symbol, sin, tan

x = Symbol('x')

ans = diff(sin(x)**2,x)

print (ans)

ans1 = diff(tan(x),x)
print (ans1)
