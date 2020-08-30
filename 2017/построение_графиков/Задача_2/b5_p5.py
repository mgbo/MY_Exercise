
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np


ax = axes3d.Axes3D(plt.figure())

t=np.arange(-5,5, 0.1)

x,y= np.meshgrid(t,t)

z = x**2 - y**2

# plot the surface
surf = ax.plot_surface(x,y,z, cmap=cm.coolwarm,linewidth=0, antialiased=False)

ax.plot_surface(x,y,z rstride=10, cstride=10 )

ax.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
