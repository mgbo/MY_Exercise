
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,2,100)

y1= x**3 + 5*x**2 +10
y2 = 3*x**2 + 10*x
y3 = 6*x + 10

fig,ax = plt.subplots() #будет график на нем

ax.plot(x,y1, color='blue', label= "y(x)")
ax.plot(x,y2, color='red', label= "y(x1)")
ax.plot(x,y3, color='magenta', label= "y(x)")

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_title("default grid") # поставить название графика

#_______________ поставили решетки ________________________

ax.grid(color='grey', which="major", axis='x', linestyle='-', linewidth=0.25)
ax.grid(color='grey', which="major", axis='y', linestyle='-', linewidth=0.25)

ax.set_xlim(-5,2) #определить диапазоны осей


ax.legend()
plt.show()

fig.savefig('pic_1.png')
