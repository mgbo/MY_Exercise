
# -*- coding: utf-8 -*-

import sympy as sm
from sympy.plotting import plot

x = sm.Symbol('x')
k = sm.Symbol('k')
w = sm.Function('w')(x) # волновая функция


fun = sm.diff(w,x,x,)+k*w
sm.pprint(fun)


eq = sm.Eq(fun,0)
print "дифференциальное уравнение : "
sm.pprint(eq)

sol = sm.dsolve(eq)
print "решение дифференциального уравнения "
sm.pprint(sol)

