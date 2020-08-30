

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(111, polar=True)

t=np.arange(0, 8*np.pi,0.01)

r=2*t


plt.plot(t,r, lw="2")

plt.grid(True)

plt.show()
