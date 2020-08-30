
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig,ax1=plt.subplots(figsize=(8,4))

t=np.arange(0, 2*np.pi, 0.01)

x=np.sin(5*t+np.pi/2)
y=np.sin(6*t)


ax1.plot(x, y, color="blue")

plt.show()
