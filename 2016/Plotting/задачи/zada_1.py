
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,10.01,0.01)

plt.xscale('log')
plt.yscale('log')

plt.xlabel(r'$x$')

plt.plot(x,x**x)

plt.show()
