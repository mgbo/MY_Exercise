
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d.axes3d import Axes3D, get_test_data

fig=plt.figure()

ax = fig.add_subplot(111, projection='3d') 

i = np.arange(-5, 5, 0.05)
X,Y = np.meshgrid(i,i)

Z=(np.sin(X)*np.sin(X))/X*Y

#X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3, color="darkgrey")

plt.show()
