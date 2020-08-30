
import matplotlib.pyplot as plt
import numpy as np

t=np.arange(0, 5*np.pi,0.01)

x=t*np.sin(t)
y=t*np.cos(t)

plt.plot(x,y, lw="1")

plt.axis('equal')
plt.grid(True)

plt.show()
