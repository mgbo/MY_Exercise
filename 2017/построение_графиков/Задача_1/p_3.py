
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-1, 4, 0.01)
y=np.arange(0, 5, 1)

plt.title("Экспериментальные точки и теоретическая кривая")

plt.ylabel("y")
plt.xlabel("x")


plt.plot (x, x**2, color="blue")
plt.plot (y, y**2, 'gs')

plt.grid(color="grey", which="major", axis="y", linestyle=":", linewidth=0.25)
plt.grid(color="grey", which="major", axis="x", linestyle=":", linewidth=0.25)

plt.xlim(-1,5)

plt.show()


