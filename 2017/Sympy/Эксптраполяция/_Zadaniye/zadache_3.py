
#-*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import*
#from scipy.linalg import*
from pylab import*
import matplotlib.pyplot as plt

#-------- читаем данные из файлов ------------
x = fromfile('x_data3.txt',float,sep='\n')
y = fromfile('y_data3.txt',float,sep='\n')

# ------------------- функция ----------------
def f_1(x,b0,b1,b2):
	return b0 + b1*np.exp(-b2*x**2)

def f_2(x,a,b,c):
	return np.sin(a*x + b)+c

# --------------- Решение функция f_1 -------------------
beta_opt,beta_cov = curve_fit(f_1,x,y)
print (beta_opt)

lin_div = sum(beta_cov[0])
print (lin_div)

residuals = y - f_1(x,*beta_opt)
fres = sum(residuals**2)
print (fres)

# --------------- Решение функция f_2 -------------------
beta_opt2,beta_cov2 = curve_fit(f_2,x,y)
print (beta_opt2)

lin_div2 = sum(beta_cov2[0])
print (lin_div2)

residuals2 = y - f_2(x,*beta_opt2)
fres2 = sum(residuals2**2)
print (fres2)

#----------- Рисуем график ------------------
xdata = np.linspace(x[0],x[-1],100)

fig,ax = plt.subplots()
ax.scatter(x,y,label="from file data")
ax.plot(xdata,f_1(xdata,*beta_opt),'b',label="function f_1(x)")
ax.plot(xdata,f_2(xdata,*beta_opt2),'r',label="function f_2(x)")

ax.legend()
ax.set_xlim(0,x[-1])
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x)$", fontsize=18)
ax.grid(color="black", which="both", linestyle=":", linewidth=1)

plt.show()
