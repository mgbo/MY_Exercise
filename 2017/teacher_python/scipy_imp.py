
# -*- coding: utf-8 -*-
from pylab import *
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def f(x, a, b):
    return a*x/(b+x)
    
def f2(x, k, c):
	return k*x+c
    
xdata = fromfile('x_data2.txt', sep='\n')   
ydata = fromfile('y_data2.txt', sep='\n')   


# ------ f = a*x/(b+x)
beta_opt, beta_cov = curve_fit(f, xdata, ydata)
print(beta_opt)

lin_dev =  sum(beta_cov[0])
print (lin_dev)

residuals = ydata - f(xdata,*beta_opt)
fres = sum(residuals**2)
print (fres)

# -------- k*x+c

beta_opt2, beta_cov2 = curve_fit(f2, xdata, ydata)
print(beta_opt)

lin_dev =  sum(beta_cov2[0])
print (lin_dev)

residuals = ydata - f(xdata,*beta_opt2)
fres = sum(residuals**2)
print (fres)

# ---- plot

x = np.linspace(xdata[0], xdata[-1], 100)

fig, ax = plt.subplots()
ax.scatter(xdata, ydata)
ax.plot(x, f(x, *beta_opt), 'b', lw=2, label="%fx/(%f+x)"%(beta_opt[0], beta_opt[1]))
ax.plot(x, f2(x, *beta_opt2), 'r', lw=2, label="%fx+%f"%(beta_opt2[0], beta_opt2[1]))
ax.legend()
ax.set_xlim(0, 5)
ax.set_xlabel(r"$x$", fontsize=18)
ax.set_ylabel(r"$f(x, \beta)$", fontsize=18)
plt.show()
