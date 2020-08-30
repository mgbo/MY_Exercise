
# -*- coding:utf-8 -*-

import sympy as sm
from sympy.plotting import plot

x = sm.Symbol('x')
fun = x**2
print fun

df = fun.diff(x)
print ("diff equal : ")
print df

T_1 = fun.subs({x:9})+df.subs({x:9})*(x-9)
print "tangent equ : "
print T_1

plot(fun,T_1,(x,0,15))