
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()

x=np.arange(-1, 1, 0.01)

plt.subplot(121)
p1=plt.plot(x, x**2, color="red", label="x**2")
plt.plot(x, np.sin(10*x), color="blue", label="sin(10*x)")

#plt.text(0,.9, r'sin(10*x)')

plt.grid(color='grey', which="major", axis='x', linestyle=':', linewidth=0.25)
plt.grid(color='grey', which="major", axis='y', linestyle=':', linewidth=0.25)

plt.xlim(-1,1)
plt.ylim(-1,1)
plt.legend(loc=3)


plt.subplot(122)
x1=np.arange(0, 4, 0.01)
y=np.arange(0,5, 1)
plt.plot (x1, x1**2+1, color="blue", label="x**2")
plt.plot (y, y*y, 'go', label="y**2")

plt.grid(color='grey', which="major", axis='x', linestyle=':', linewidth=0.25)
plt.grid(color='grey', which="major", axis='y', linestyle=':', linewidth=0.25)


plt.show()

fig.savefig('P_4.png')
