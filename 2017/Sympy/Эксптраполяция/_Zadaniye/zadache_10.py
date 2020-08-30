
#-*- coding:utf-8 -*-
from pylab import*
import numpy as np
from scipy.optimize import*
import matplotlib.pyplot as pyt

def f_2(x,k,a,b,c):
	return k*np.sin(a*x+b)+c

def f_1(x,a,x0,sigma):
	a*np.exp(-(x-x0)**(2/(2*sigma**2)))

x = fromfile('x_data10.txt',sep='\n')
y = fromfile('y_data10.txt',sep='\n')

# --------------- Решение функция f_1 -------------------
beta_opt,beta_cov = curve_fit(f_1,x,y)
print (beta_opt)

lin_div = sum(beta_cov[0])
print (lin_div)

residuals = y - f_1(x,*beta_opt)
fres = sum(residuals**2)
print (fres)

# --------------- Решение функция f_2 -------------------


#----------- Рисуем график ------------------
xdata = np.linspace(x[0],x[-1],100)

fig,ax = plt.subplots()
ax.scatter(x,y,label="from file data")
ax.plot(xdata,f_1(xdata,*beta_opt),'b',label="function f_1(x)")
#ax.plot(xdata,f_2(xdata,*beta_opt2),'r',label="function f_2(x)")

ax.legend()
ax.set_xlim(0,x[-1])
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x)$", fontsize=18)
ax.grid(color="black", which="both", linestyle=":", linewidth=1)

plt.show()






