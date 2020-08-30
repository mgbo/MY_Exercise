
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
from sympy import*

x = symbols('x')

e1 = x**2 - 5
e2 = -x**2 + 3

a_eq = e2 - (e1)
pprint (a_eq)

a = solve(a_eq,x)
print (a)

ans = integrate(a_eq,(x,-1,a[1]))
print ("Площадь графика : ",ans)

#--------------- рисование графика -------------
x = np.linspace(-4,4,100)

eq1 = x**2 - 5
eq2 = -x**2 + 3

fig,ax = plt.subplots()
ax.plot(x, eq1, color ="blue", label="y(x)")
ax.plot(x, eq2, color ="red", label="y'(x)")
ax.axvline(x=-1,color ="green")

ax.legend()
ax.set_title(r'$x^2 - 5$')

ax.set_ylim(-5,5)
ax.set_xlim(-4,4)
eq0 = Eq(x,-1)
# для того чтобы красить 
#ax.fill_between(x, eq1, eq2, where= [eq2>=eq1, x>-1], facecolor='wheat')
ax.fill_between(x, eq0, eq1, eq2, where= None, facecolor='wheat')

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.grid(color="blue", which="major", axis='x', linestyle=':', linewidth=1)
ax.grid(color="blue", which="major", axis='y', linestyle=':', linewidth=1)

plt.show()
