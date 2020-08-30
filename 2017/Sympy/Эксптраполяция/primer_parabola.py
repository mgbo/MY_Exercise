
#-*- coding:utf-8 -*-

from numpy import *
from numpy.random import *

delta=1.0
x=linspace(-5,5,11)
y=x**2+delta*(rand(11)-0.5)
x+=delta*(rand(11)-0.5)

x.tofile('x_data.txt', '\n')
y.tofile('y_data.txt', '\n')

from pylab import *
from scipy.linalg import *
import matplotlib.pyplot as plt

x = fromfile('x_data.txt',float,sep='\n')
y = fromfile('y_data.txt',float,sep='\n')

# задаем вектор m = [x**2, x, E]
m = vstack((x**2,x,ones(11))).T
print (m)

# находим коэффициенты при составляющих вектора m
s = lstsq(m,y)[0]
print ("S : ",s)

# на отрезке [-5,5]
x_prec = linspace(-5,5,100)
fig,ax = plt.subplots()

# нарисуем теорическую крувую
ax.plot(x_prec, x_prec**2, '--', lw=2, label="Nornal data $x^2$")

#рисуем точки
ax.plot(x,y,'D',lw=2, label="Random data")

# рисуем кривую вида y = ax<sup>2</sup> + bx + c, подставляя из решения коэффициенты s[0], s[1], s[2]
ax.plot(x_prec,s[0]*x_prec**2 + s[1]*x_prec + s[2], '-',lw=2, label= "Approximation")

ax.grid(color="blue", which="major", axis='x', linestyle=':', linewidth=1)
ax.grid(color="blue", which="major", axis='y', linestyle=':', linewidth=1)
ax.set_xlim(-6,6)
ax.set_ylim(-1,20)

ax.legend()
ax.grid(True)
plt.show()
fig.savefig('1.png')









