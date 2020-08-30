
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(8, 2.5), facecolor="#f1f1f1")

# axes coordinates as fractions of the canvas width and height
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8 # задаем значения переменных
ax = fig.add_axes((left, bottom, width, height), axisbg="#e1e1e1")

x = np.linspace(-2, 2, 1000)
y1 = np.cos(40 * x)
y2 = np.exp(-x**2)

ax.plot(x, y1 * y2)
ax.plot(x, y2, 'g')
ax.plot(x, -y2, 'g')
ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()
fig.savefig("1a.png", dpi=100, facecolor="#f1f1f1")

'''
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import axes3d
ax=axes3d.Axes3D(plt.figure())



i=np.arange(-1, 1, 0.01)
x,y=np.meshgrid(i,i)
z=x**2-y**2

ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

plt.show()
'''
