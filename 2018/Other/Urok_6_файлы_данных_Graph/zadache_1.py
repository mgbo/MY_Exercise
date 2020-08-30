
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10,0.01)
y=x**x

plt.xscale('log')
plt.yscale('log')


plt.plot(x,y,color="blue",label=r'$x^x$')
plt.legend(loc=1)

plt.xlabel("x")
plt.ylabel("x в степении x")

plt.xlim(1,10)

plt.show()
