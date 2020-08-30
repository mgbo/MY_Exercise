#-*- coding:utf-8 -*-

from sympy import*
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

eq1 = -x**2 + 3
eq2 = x**2 - 5
eq3 = 2

eq = eq1 - eq2

a = solve(eq,x)
print (a)

b = solve(-x**2 + 3 -2,x)
print (b)

in_eq = integrate(eq,(x,a[0],a[1]))-integrate(-x**2 + 3 -2,(x,b[0],b[1]))

pprint (in_eq.n())

#--------------- рисование графика -------------

x1 = np.linspace(-4,4,100)
e1 = -x1**2 + 3
e2 = x1**2 - 5
e3 = 2
ax = plt.subplot()

ax.plot(x1,e1, color="blue", lw=2, label=r'$-x^2+3$')
ax.plot(x1,e2, color="red", lw=2, label=r'$x^2-5$')
#ax.plot(e3, color="green", lw=2, label="2")
#ax.axvline(x1=2,color="green")

ax.set_xlim(-4,4)
ax.set_ylim(-5,5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.grid(color="blue", which="both", linestyle=':',linewidth=1)

ax.fill_between(x1,e1,e2, where=e1>e2, facecolor='wheat')
plt.show()





