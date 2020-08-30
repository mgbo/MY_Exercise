
'''
import matplotlib.pyplot as plt

import numpy as np

x=np.arange(-10,10,0.01)
t=np.arange(-10,10,1)

plt.plot(x,x**2,t,t**2,'ro')

plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(111, polar=True)

phi=np.arange(0,2*np.pi,0.01)
rho=2*phi

plt.plot(phi,rho,lw=2)
#plt.grid(True)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

t=np.arange(0,2*np.pi,0.01)
r=4

plt.plot(r*np.cos(t),r*np.sin(t),lw=3)

plt.axis('equal')
plt.show()
