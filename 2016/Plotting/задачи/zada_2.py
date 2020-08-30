
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-1,1,0.01)

plt.plot(x,np.sin(10*x),x,x**2,'r')
plt.text(0,0.5,r'sin(10*x)')
plt.text(0.1,0.4,r'x^2')

plt.show()
