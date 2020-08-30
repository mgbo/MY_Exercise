
# -*- coding: utf-8 -*-

import sympy as sm
from sympy.plotting import plot

t = sm.symbols('t') #time
x = sm.Function ('x') # растояние
w = sm.Symbol('w', positive = True)

# запишем уравнение
# x'' + x * w^2 = 0

fun = sm.diff(x(t),t,t) + w**2 * x(t)

eq = sm.Eq(fun,0)

print ("Equation : ")
print (eq)

# решим уравнение в общем виде
sol = sm.dsolve(eq)
print ("Решение в общем виде : ")
print (sol)

print ("\n--------\n")

#  для того чтобы выражать только направо уравнения
x = sol.rhs

print (x)
print (fun)

# проверим, что решение найдено верно

if sm.diff(x,t,t)+w**2 * x == 0:
	print ("\nCheck : sm.diff(x,t,t) + w**2 * x = 0 ------ OK" )

print ("with begin conditions ")

# учем начальные условия
# x(0) = L => x(0) - L =0
# x'(0) = 0

# запишем начальные условия через найденные решения

L = sm.symbols('L')

T1 = x.subs({t:0}) - L
print (sm.diff(x,t))

T2 = sm.diff(x,t).subs({t:0})
print (T1,T2)

C1,C2 = sm.symbols("C1,C2")
solconst = sm.solve([T1,T2],[C1,C2])
print (solconst)






