
# -*- coding:utf-8 -*-

from sympy import*

x,t,a = symbols('x t a',positive=True)

#i = Integral((x+1)/(x**2 + 2*x - 5),x)
i = Integral(1/(x+a),x)
pprint (i)

it = i.transform(x+a,t)
pprint (it)

ans = it.doit()

pprint (ans)