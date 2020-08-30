
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(111, polar=True) #Полярная система координат

t=np.arange(0, 2*np.pi, 0.001)

r=2-2*np.sin(t)+np.sin(t)*(np.sqrt(np.abs(np.cos(t)))/np.sin(t)+1.4)


plt.plot(t,r, lw=1)
plt.grid(True)

plt.show()
