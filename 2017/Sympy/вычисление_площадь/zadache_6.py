#-*- coding:utf-8 -*-

from sympy import*

x = symbols('x')

eq_a = 2 - x + 3
a = solve(eq_a,x,dic = True)
print (a)

eq_b = 2 + x + 3
b = solve(eq_b,x,dic = True)
print (b)

ing_1 = integrate(eq_a,(x,0,a[0]))
#print (ing_1)

ing_2 = integrate(eq_b,(x,b[0],0))
#print (ing_2)

ans = ing_2 + ing_1
print ("последный ответ : ",ans)
