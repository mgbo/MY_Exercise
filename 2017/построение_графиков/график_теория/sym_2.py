
# -*- coding: utf-8 -*-
'''
В сосуд, содержащий 10 л воды, 
непрерывно поступает со скоростью 2 л в минуту раствор, 
в каждом литре которого содержится 0.3 кг соли. 
Поступающий в сосуд раствор перемешивается с водой и 
смесь вытекает с той же скоростью. 
Сколько соли будет в растворе через 5 минут? 
'''

# y' = 0.6 - 0.2*y

import sympy as sm
from sympy.plotting import plot

t = sm.symbols('t')        # time
y = sm.Function('y')

# запишем уравнение
# y' = 0.6 - 0.2*y   => fun = 0 
fun = sm.diff(y(t), t) - (0.6 - 0.2*y(t) )

eq = sm.Eq(fun, 0)
print 'Equation :'
print eq


# решим уравнение в общем виде
sol = sm.dsolve(eq)
print 'Solition in general form:'
print sol

ysol = sol.rhs
print 'ysol ='
print ysol

# ysol(0) = 0
ysol.subs(t,0)
print ysol.subs(t,0)

C1 = sm.symbols("C1")
c1_sol = sm.solve( ysol.subs(t,0), C1)
print 'C1='
print c1_sol

y1 = ysol.subs(C1, -3)
print y1

res = y1.subs(t, 5)
print 'Соли в сосуде через 5 минут'
print res

plot(y1, (t, 0, 5))

