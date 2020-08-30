
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8,2.5),facecolor="#f1f1f1")
# определить размер фото

left, bottom, width, height =0.1,0.1,0.8,0.8
ax= fig.add_axes((left, bottom, width, height),axisbg="#e1e1e1")

x=np.linspace(-2, 2,1000)
y1= np.cos(40*x)
y2= np.exp(-x**2)

ax.plot(x, y1*y2)
plt.plot(x,y2, 'g')
plt.plot(x,-y2, 'g')

ax.set_xlim(-5,35)
ax.set_ylim(-1,1)
ax.axis('tight')



plt.show()
fig.savefig("theory_2.png", dpi=100, facecolor= "#f1f1f1")
