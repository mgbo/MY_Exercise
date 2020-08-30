
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from sympy import*

x = symbols('x')

eq1 = -x + 3
eq2 = x + 3
eq3 = -2

eq_a = x + 3 + 2
a = solve(eq_a,x,dic = True)
print (a)

eq_b = -x + 3 +2
b = solve(eq_b,x)
print (b)

ans = integrate(eq_a,(x,a[0],0)) + integrate(eq_b,(x,0,b[0])) 
print (ans)

#--------------- рисование графика -------------

x1 = np.linspace(-7,7,100)
e1 = -x1 + 3
e2 = x1 + 3
e3 = -2
ax = plt.subplot()

ax.plot(x1,e1, color="blue", lw=2, label=r'$-x+3$')
ax.plot(x1,e2, color="red", lw=2, label=r'$x+3$')
ax.axhline(y=e3,color="green",lw=3)
ax.legend()

#ax.plot(e3, color="green", lw=2, label="2")

ax.set_xlim(-7,7)
ax.set_ylim(-5,5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.grid(color="blue", which="both", linestyle=':',linewidth=1)
#ax.fill_between(x1,e1,e2, where=e2>e1, facecolor='wheat')
#ax.fill_between(x1,e1,y, where=e1>e2, facecolor='wheat')

plt.show()


