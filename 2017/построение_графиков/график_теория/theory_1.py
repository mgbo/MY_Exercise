
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.use('Agg') # не рисовать на экране

fig,ax=plt.subplots() #будет 1 график, на нем

x=np.linspace(-5,2,100) #от -5 до 2 , 100 точек

y1= x**3 + 5*x**2 + 10
y2= 3*x**2 + 10*x
y3= 6*x + 10

ax.plot(x,y1, color="green", label="y(x)")
ax.plot(x,y2, color="red", label="y'(x)")
ax.plot(x,y3, color="blue", label="y''(x)")

ax.set_xlabel("codomain")
ax.set_ylabel("function")

ax.legend(ncol=3, loc=2, bbox_to_anchor=(1,1))

plt.grid(True)
plt.show()

fig.savefig('theory_1.png')
