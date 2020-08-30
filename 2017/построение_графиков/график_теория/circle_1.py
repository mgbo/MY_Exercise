
import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0, 2*np.pi, 0.01)

r=5

plt.plot(r*np.sin(t),r*np.cos(t),lw=5)

plt.axis('equal')

plt.show()

