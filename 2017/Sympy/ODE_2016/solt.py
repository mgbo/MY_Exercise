
# -*- coding: utf-8 -*-


# по условию задачи
# y' = 0.6 - 0.2* y(t)

import sympy as sm
from sympy.plotting import plot
import numpy as np
import matplotlib.pyplot as plt

t = sm.symbols('t') # time
y = sm.Symbol('y')

fun = sm.diff(y(t),t) -(0.6 - 0.2 * y(t))
print "Equation : "
print fun

eq = sm.Eq(fun,0)

print "\nдифференциальное уравниение в общем виде "
print (eq)

# решим уравнение в общем виде
sol = sm.dsolve(eq)
print (sol)
print "Решение ДУ "
ysol = sol.rhs
print ysol

# Так как при t =0 соли в сосуде не было , то y(0)=0
# ysol (0) = 0
ysol.subs(t,0)
print "if t=0 , in the vassel no solt y(t)\nif y(0)=0"
print (ysol.subs(t,0))

# для того чтобы наити С1
C1 = sm.symbols("C1")
C1_sol = sm.solve(ysol.subs(t,0),C1)
print "C1 = "
print C1_sol

# for y(t)
y1 = ysol.subs(C1,-3)
print "последное решение ДУ задачи "
print (y1)

# Сколько соли будет в сосуде через 5 минут
ans = y1.subs(t,5)
print ("соли в сосуде через 5 минут")
print (ans)

plot(y1, (t,0,5)) # Впросы
'''
t = np.arange(0,5,0.01)
y = 3 - 3*np.exp(-0.2*t)

plt.plot(y,t,'r')
plt.ylabel(r'$3-3*e^(-0.2*t)$', fontsize=16, color = "red")
plt.xlabel(r'$Time$', fontsize = 16, color = "red")
plt.grid(True)
plt.show()
'''

