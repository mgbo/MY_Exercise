
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0, 5, 0.1)
y=np.arange(0, 5, 0.1)
r=5

x1=np.sqrt(r**2-y**2)


print x1


plt.plot(-x1,x1)
plt.plot(x1,-x1)
#plt.plot(-(np.sqrt(r**2-x**2)), np.sqrt(r**2-x**2))


plt.show()
