
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


ax = plt.subplots()

x = np.linspace(-2, 2, 1000)

y1 = np.cos(40*x)
y2 = np.exp(-x**2)

ax.plot(x,y1*y2)

ax.set_xlim(-5,35)
ax.set_ylim(-1,1)




plt.show()
