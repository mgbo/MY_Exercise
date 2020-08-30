
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import axes3d
ax=axes3d.Axes3D(plt.figure())

i=np.arange(-1,1,0.01)

x,y=np.meshgrid(i,i)

z=x**2 - y**2

ax.plot_wireframe(x,y,z, rstride=10, cstride=10)

plt.show()
