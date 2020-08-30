
#-*- coding:utf-8 -*-

from sympy import*

x = symbols('x',positive=True)
eq = x/(3*x**2-1)

inte_x = Integral(eq,(x,0,1))
pprint (inte_x)

ans = integrate(eq,(x,0,1))
pprint (ans.n())