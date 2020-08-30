
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(-10,10.01,0.01);
t=np.arange(-10,11,1)

#subplot 1
plt.subplot(221)
plt.plot(x,np.sin(x))
plt.title(r'$sin(x)$')
plt.grid(True)


#subplot 2
plt.subplot(222)
plt.plot(x,np.cos(x),'g')
plt.axis('equal')
plt.grid(True)
plt.title(r'$\cos(x)$')

#subplot 3
plt.subplot(223)
plt.plot(x,x**2,t,t**2,'ro')
plt.title(r'$x^2$')
plt.grid(True)

plt.show()
