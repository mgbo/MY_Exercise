
#-*- coding:utf-8 -*-
from sympy import*
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

eq1 = x**2 - 5
eq2 = -x**2 + 3

eq = x**2 - 5 + x**2 - 3

a = solve(eq,x)
pprint (a)

ans = Integral(-x**2 + 3 -x**2 + 5,(x,-1,a[1]))
pprint (ans)

ans_1 = integrate(-x**2 + 3 - x**2 + 5,(x,-1,a[1]))
print ("ответ : ",ans_1)


#--------------- рисование графика -------------

x1 = np.linspace(-4,4,100)
e1 = x1**2 - 5
e2 = -x1**2 + 3
e3 = -1
ax = plt.subplot()

ax.plot(x1,e1, color="blue", lw=2, label=r'$-x+3$')
ax.plot(x1,e2, color="red", lw=2, label=r'$x+3$')
ax.axvline(x=e3,color="green",lw=3, label=r'')
ax.legend()

#ax.plot(e3, color="green", lw=2, label="2")

ax.set_xlim(-4,4)
ax.set_ylim(-5,5)

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.grid(color="blue", which="both", linestyle=':',linewidth=1)
ax.fill_between(x1,e1,e2, where=e2>e1, facecolor='wheat')
#ax.fill_between(x1,e1,y, where=e1>e2, facecolor='wheat')

plt.show()





