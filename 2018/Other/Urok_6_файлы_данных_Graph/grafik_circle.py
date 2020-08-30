
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 2*np.pi, 0.01)          # угол t от 0 до 2pi с шагом 0.01
r = 4                                    # радиус 4

plt.plot(r*np.sin(t), r*np.cos(t), lw=3) # x и у задаем как numpy функции от t
plt.axis('equal')                        # масштаб осей Х и У одинаковый (чтобы круг не был овалом)

plt.grid(color='blue',axis='x',linestyle=":",linewidth='0.25')
plt.grid(color='gray',axis='y',linestyle=":",linewidth='0.25')


plt.show()
