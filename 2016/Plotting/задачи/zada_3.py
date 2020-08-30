
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.0,18,0.01)
t=np.arange(0,18,2)

plt.plot(x,x**2,'r')
plt.plot(x,x**2,t,t**2,'go')

plt.grid(True)
plt.show()

