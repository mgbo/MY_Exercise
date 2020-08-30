
#-*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

xx = np.linspace(-4,4,100)

eq1 = xx**2 - 5
eq2 = -xx**2 + 3

fig,ax = plt.subplots()
ax.plot(xx, eq1, color ="blue", label="y(x)")
ax.plot(xx, eq2, color ="red", label="y'(x)")

ax.legend()
ax.set_title("Plot Example")

ax.set_ylim(-5,5)
ax.set_xlim(-4,4)

# для того чтобы красить 
ax.fill_between(xx, eq1, eq2, where= eq2>=eq1, facecolor='wheat')

ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

ax.grid(color="blue", which="major", axis='x', linestyle=':', linewidth=1)
ax.grid(color="blue", which="major", axis='y', linestyle=':', linewidth=1)

plt.show()
