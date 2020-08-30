
#-*- coding:utf-8 -*-
import numpy as np
from scipy.optimize import*
from scipy.linalg import*
from pylab import*
import matplotlib.pyplot as plt

#читаем данные из файлов
x = fromfile('x_data.txt',float,sep='\n')
y = fromfile('y_data.txt',float,sep='\n')

# --------- функция ----------
def f(x,b0,b1,b2):
	return b0 + b1*np.exp(-b2*x**2)

def f2(x,k,c):
	return k*x + c

#---------------- Решение для функция f ------------------ 
beta_opt,beta_cov = curve_fit(f,x,y)
print (beta_opt)

lin_dev = sum(beta_cov[0])
print (lin_dev)

residuals = y - f(x,*beta_opt)
fres = sum(residuals**2)
print (fres)

#------------- Решение для функция f2 ------------------ 
beta_opt2,beta_cov2 = curve_fit(f2,x,y)
print (beta_opt2)

lin_dev2 = sum(beta_cov2[0])
print (lin_dev2)

residuals2 = y - f2(x,*beta_opt2)
fres2 = sum(residuals2**2)
print (fres2)

#----------- Рисуем график ------------------
xdata = np.linspace(x[0],x[-1],100)

fig,ax = plt.subplots()
ax.scatter(x,y,label="from file data")
ax.plot(xdata,f(xdata,*beta_opt),'b',label="function f_1(x)")
ax.plot(xdata,f2(xdata,*beta_opt2),'r',label="function f_2(x)")

ax.legend()
ax.set_xlim(0,x[-1])
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x)$", fontsize=18)
plt.show()

