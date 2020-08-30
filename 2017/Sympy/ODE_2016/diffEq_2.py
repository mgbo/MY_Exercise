
# -*- coding:utf-8 -*-

import sympy  as sm

t = sm.symbols('t')
x = sm.Function('x')

w = sm.Symbol('w', positive = True)

eq = sm.Eq(sm.diff(x(t),t,t)+w**2*x(t),0)

print ("дифференциальное уравнение : ")
print (eq)

sol = sm.dsolve(eq)

print ("решение дифференциальное уравниение ")
print sol

x = sol.rhs

print ("решение дифференциальное уравниение (только направо) ")
print x


df_2 = sm.diff(x,t,t)

print df_2

# для проверка

print(sm.diff(x,t,t)+w**2*x == 0)

T1 = x.subs({t:0})-L
print T1



