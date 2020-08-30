
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(-np.pi, np.pi, 0.01)

plt.subplot(131)
y1=np.sin(x)
y2=2*np.sin(x)
plt.title(r'$sin(x) and 2sin(x)$', fontsize=14)
plt.plot(x, y1, color="blue")
plt.plot(x,y2, color="green")
plt.grid(True)
plt.axis('tight')
plt.xticks([-np.pi,0,np.pi],[r'$\pi$','0',r'$\pi$'])

plt.subplot(132)
plt.title(r'$sin(x) and sin(2x)$')
plt.plot(x,np.sin(x), color="red")
plt.plot(x,np.sin(2*x), color="blue")
plt.grid(True)
plt.axis('tight')
plt.xticks([-np.pi,0,np.pi],[r'$\pi$','0',r'$\pi$'])

plt.subplot(133)
plt.title(r'$sin(x) and sin^2(x)$')
plt.plot(x, np.sin(x), color="magenta")
plt.plot(x,np.sin(x)*np.sin(x), color="blue")
plt.axis('tight')
plt.xticks([-np.pi,0,np.pi],[r'$\pi$','0',r'$\pi$'])
plt.grid(True)
plt.show()
