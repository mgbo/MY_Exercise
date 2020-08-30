
from sympy import*

x,t = symbols('x t',positive=True)

fun = (x**2 + x* log(x))/x**2
pprint (fun)

i = Integral(fun,x)
print ('\n')
pprint (i)

it = i.transform(log(x),t)
print ('\n')
pprint(it)

ans = it.doit()
pprint(ans)