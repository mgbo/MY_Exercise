
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1, 10, 0.1)
plt.xscale('log')
plt.yscale('log')

y=x**x

plt.title("пример логарифимической шкалы")


plt.plot(x,y, color="blue", label=r"$y(x)$")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()

plt.xlim(1,10)
plt.ylim(1,10000000000)


plt.show()
