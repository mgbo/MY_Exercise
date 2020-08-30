
# -*- coding:utf-8 -*-

# производная неявной функции

# вычислить производную функции x**2 + 2xy + 2y**2 = 1

from sympy import*

x = symbols('x')
y = Function('y')(x)
z = symbols('z')

eq = x**2 + 2*x*y + 2*y**2 - 1

# Make a differential equation
d_eq = diff(eq,x)
pprint (d_eq)

