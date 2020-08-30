
from sympy import*

x = symbols('x')

fun = x*exp(x**2)
i = Integral(fun,x)
pprint(i)

u = symbols('u',positive=True)
iu = i.transform(x**2,u)
print('\n')
pprint(iu)


ans = iu.doit()
pprint (ans)
