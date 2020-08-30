
# -*- coding:utf-8 -*-

from sympy import*

# производная неявной функции

x = symbols('x')
y = Function('y')(x)
z = symbols('z')

eq = x*x + 2*x*y + 2*y*y - 1
pprint (eq)

# Make a differential equation
d_eq = diff(eq,x)
pprint (d_eq)


