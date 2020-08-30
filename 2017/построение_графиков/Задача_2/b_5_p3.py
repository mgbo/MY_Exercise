

import matplotlib.pyplot as plt 
import numpy as np

t=np.arange(0, 2*np.pi, 0.01)

x=20*(np.cos(t)+np.cos(5*t)/5)
y=20*(np.sin(t)-np.sin(5*t)/5)

plt.plot(x,y,'r')

plt.grid()
plt.show()
