
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-1, 1, 0.01)

plt.title(r"$корни уравнения $sin(x)=x^2$ - точка пересечениях кривых$")
plt.plot(x, x**2, color="red", label=r'$sin(10.x)$')
plt.plot(x, np.sin(10*x), color="blue", label=r'$x^2$')

#plt.text(0,.9, r'$sin(10*x)$')
plt.xticks([-1,-0.5,0.0,0.5,1.0])

plt.legend(loc=3)

plt.grid(color='grey', which="major", axis='x', linestyle=':', linewidth=0.25)
plt.grid(color='grey', which="major", axis='y', linestyle=':', linewidth=0.25)

plt.xlim(-1,1)
plt.ylim(-1,1)

plt.show()

