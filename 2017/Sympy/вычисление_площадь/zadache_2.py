
#-*- coding:utf-8 -*-

from sympy import*
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

eq2 = 5 - x**2
eq1 = 1/(x+4)-4


#a = solve(eq,x)
#print (a)

#ans = integrate(eq,(x,a[0],a[1]))
#print (ans)

#--------------- рисование графика -------------

x1 = np.linspace(-4,4,100)
e1 = 5 - x1**2
e2 = 1/(x1+4) - 4

ax = plt.subplot()
ax.plot(x1,e1, color='blue', lw=2, label=r'$5-x^2$')
ax.plot(x1,e2, color='red', lw=2, label=r'$1/(x+4)-4$')
ax.legend(loc=1)

ax.set_ylim(-5,5)
ax.set_xlim(-4,4)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.fill_between(x1,e1,e2, where=e1>e2, facecolor='wheat')
ax.grid(color="black", which="both", linestyle=":", linewidth=1)

plt.show()







