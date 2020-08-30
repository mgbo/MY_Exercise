
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-5, 2, 100) # от -5 до 2 сделать 100 точек

y1= x**3 + 5*x**2 + 10
y2= 3*x**2 + 10*x
y3= 6*x + 10

fig,ax =plt.subplots() # будет 1 график на нем

ax.plot(x,y1, color="blue" , label="y(x)")
ax.plot(x,y2, color="red" , label="y'(x)")
ax.plot(x,y3, color="green", label="y''(x)")

ax.set_xlabel("x")
ax.set_ylabel("y")

ax.legend() #показать условие обозначения


plt.show()
fig.savefig('1.png')

'''
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10, 10.01, 0.01) # от -10 до 10.01 с шагом 0.01 (>1000 точек)
t=np.arange(-10, 11, 1) # с шагом 1 (20 точек)

fig=plt.figure()

#subplot 1
plt.subplot(221)            # первая область
plt.plot(x, np.sin(x))      # sin(x) на [-10, 10] цветом по умолчанию
plt.title(r'$\sin(x)$')     # заголовок "sin(x)"
plt.grid(True)              # рисовать решетку

#subplot 2
plt.subplot(222)            # вторая область
plt.plot(x, np.cos(x), 'g') # cos(x) на [-10, 10] зеленая линия
plt.axis('equal')           # одинаковый масштаб по осям Х и Y
plt.grid(True)              # рисовать решетку
plt.title(r'$\cos(x)$')     # заголовок "cos(x)"

#subplot 3
plt.subplot(223)            # третья область
plt.plot(x, x**2, t, t**2, 'ro') # 2 графика, первый линией, второй красными кругами
plt.title(r'$x^2$')         # заголовок "x2"
                            # решетки нет

#subplot 4
plt.subplot(224)            # четвертая область
plt.plot(x, x)              # прямая y=x
                            # оси с подписями нарисовать
                            # левую в центре
plt.subplot(224).spines['left'].set_position('center')
                            # нижнюю в центре
plt.subplot(224).spines['bottom'].set_position('center')
plt.title(r'$x$')           # заголовок "x"
plt.grid(True)

plt.show()
fig.savefig('2.png')
'''
