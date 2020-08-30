
# -*- coding: utf-8 -*-

import sympy as sm
from sympy.plotting import plot

t = sm.symbols('t') #time
x = sm.Function('x')
w = sm.Symbol('w', positive = True)

fun = sm.diff(x(t),t,t)+ w**2 * x(t)
#eq = sm.Eq(sm.diff(x(t),t,t)+w**2 * x(t),0)
eq = sm.Eq(fun,0)

print ('\nEquation DE :')
sm.pprint(eq)

sol = sm.dsolve(eq)
sm.pprint (sol)

x = sol.rhs
sm.pprint (x)

print ("\n-------\n")
print (fun)

# запишем начальные условия через найденные решения
L = sm.symbols('L')
T1 = x.subs({t:0})- L # первый дифференциальное
T21 = sm.diff(x,t)

print ("T1 : ")
print (T1)
print (T21)

T2 = T21.subs({t:0}) # второй дифферен
print ("T2 : ")
print (T2)

# решим полученную систему относитлеьно неизвестных констант с1 и с2
C1,C2 = sm.symbols("C1 C2")
solconst = sm.solve([T1,T2],[C1,C2]) # не поятно
print (solconst)

# подставим константы С1 и С2 в решение и получим ответ x(t) = ---

res = x.subs(solconst)
print ("последный ответ ")
#print 'x(t) = '+ str(res)
print ('x(t) = ',(res))

m = sm.symbols('m', float=True, positive = True)
k = sm.symbols('k', float = True, positive = True)
w = sm.Symbol('w', positive = True)

wo = sm.solve(w**2 -k/m,w) # w^2-k/m 
wo= wo[0] # w^2 - k/m = 0 => 

print ('w = ',wo)
#print 'w = '+str(wo)

res0 = res.subs({w:wo})
print ('x(t) = ', res0)

# подставим численные условия задачи
# получим ответ в виде численной формулы

x = res0.subs({L:0.1,k:5,m:1})
print ('x(t) = '+ str(x))
print ('x(1) = '+ str(res0.subs({t:1,L:0.1,k:5,m:1})))

# и в виде числа
print (res0.subs({t:3,L:0.1,k:5,m:1}).n())

plot (x,(t,0,5))






