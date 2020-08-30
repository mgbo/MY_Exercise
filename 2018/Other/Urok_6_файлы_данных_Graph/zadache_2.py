
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.arange(-1,1,0.01)

y1 = np.sin(10*x)
y2 = x*x

plt.plot(x, y1, color="blue",label=r'$sin(10*x)$')
plt.plot(x, y2, color="red",label=r'$x^x$')

plt.legend(loc=3)

plt.title(r'Корни уравнения $sin(x)=x^2$ - точки пересечения кривых')


plt.grid(color="blue", axis="x", linestyle=":", linewidth="0.25")
plt.grid(color="blue", axis="y", linestyle=":", linewidth="0.25")

plt.xlim(-1,1)
plt.ylim(-1,1)

fig.savefig('2.png')
plt.show()


