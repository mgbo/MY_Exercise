
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(111, polar=True)


t=np.arange(0,2*np.pi,0.01)

x=np.sin(6*t)

plt.plot(t,x*x, 'r')

plt.show()
