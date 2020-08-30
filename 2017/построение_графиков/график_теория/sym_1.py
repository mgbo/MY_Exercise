
# -*- coding: utf-8 -*-
'''
Груз на горизонтальной пружине. Трения нет. Внешней силы нет. 
'''

'''
Дано: На пружине жесткостью k закреплен груз массой M. От положения равновесия груз отвели на расстояние L и отпустили. Трением в системе пренебречь.
Найти: Уравнение движения груза x(t)
Вычислить: х через 1 секунду от начала колебаний, для пружины жесткостью k = 5 Н/м и груза массой 1 кг, если первоначальное отклонение L = 0.1 м.

Считаем x=0 положение, где пружина находится в положении равновесия (не растянута и не сжата).
На груз действует сила упругости F = -kx
По второму закону Ньютона ma = F = -kx
Ускорение a - это вторая производная по времени от x(t), т.е.
mx'' = -kx
x'' + (k/m)*x = 0
Заменим отношение k/m на w2. (Это даст требование, что w - не отрицательное).
x'' + w**2 * x = 0
'''

import sympy as sm
from sympy.plotting import plot

t = sm.symbols('t')        # time
x = sm.Function('x')
w = sm.Symbol('w', positive=True)

# запишем уравнение
# x'' + x * w**2 = 0 
fun = sm.diff(x(t), t, t) + w**2 * x(t)
eq = sm.Eq(fun, 0)
print 'Equation :'
print eq

# решим уравнение в общем виде
sol = sm.dsolve(eq)
print 'Solition in general form:'
print sol

print '\n---\n'
# gf = fun.subs({x,xsol})
# print gf
x = sol.rhs
print 'sol.rhs = '
print x
print fun

# проверим, что решение найдено верно
# хочу тут не руками копи-пастить, а использовать fun и проверить - является ли решением или нет
if sm.diff(x,t,t) + w**2 *x == 0 :
  print 'Check: sm.diff(x,t,t) + w**2 *x == 0   ..... OK'

print 'With begin conditions:'
 
# Учтем начальные условия:
# x(0) = L   => x(0) - L = 0
# x'(0) = 0

# запишем начальные условия через найденные решения
L = sm.symbols('L')
T1 = x.subs({t:0}) -L
T2 = sm.diff(x, t).subs({t:0})
print T1, T2

# решим полученную систему относительно неизвестных констант C1 и C2
C1, C2 = sm.symbols("C1 C2")
solconst = sm.solve([T1, T2], [C1, C2])
print solconst

# подставим константы С1 и С2 в решение и получим ответ x(t) = ...
res = x.subs(solconst)
print 'x(t)='+str(res)

m = sm.symbols('m', float=True, positive=True)
k = sm.symbols('k', float=True, positive=True)
w = sm.Symbol('w', positive=True)
w0= sm.solve(w**2 - k/m, w)
w0=w0[0]
print 'w='+str(w0)

res0 = res.subs({w:w0})
print 'x(t)='+str(res0)

# подставим численные условия задачи
# получим ответ в виде численной формулы
x = res0.subs({L:0.1, k:5, m:1})
print 'x(t)='+str(x)
print 'x(1)='+str(res0.subs({t:1, L:0.1, k:5, m:1}))
# и в виде числа
print res0.subs({t:1, L:0.1, k:5, m:1}).n()

plot(x, (t, 0, 5))
