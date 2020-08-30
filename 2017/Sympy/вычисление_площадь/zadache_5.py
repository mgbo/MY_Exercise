
#-*- coding:utf-8 -*-

from sympy import*

x = symbols('x')

eq1 = x*x - 5
eq2 = 2

a_eq = eq2 - eq1

a = solve(a_eq, x, dic=True)
print (a)

ans = integrate(a_eq,(x,-2,a[1]))
pprint (ans)

pprint (together(ans).n())

