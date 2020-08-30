import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0,2*np.pi,0.01)
print "t : ",t

r=4

plt.plot(r*np.sin(t),r*np.cos(t),lw=1)

plt.axis('equal')
plt.grid(True)

plt.show()
