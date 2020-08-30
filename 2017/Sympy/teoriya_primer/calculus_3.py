
# check, that differentiation

from sympy import limit,tan,Symbol,pprint
from sympy.abc import delta
x = Symbol("x")

ans = limit((x**2+delta)-x**2/delta,delta,0)

pprint (ans)
