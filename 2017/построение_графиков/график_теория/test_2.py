
'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
'''

'''
import matplotlib.pyplot as plt
plt.plot([1,2,3,4],[1,4,9,16],'ro')
plt.axis([0,6,0,18])
plt.grid(True)
plt.show()
'''

'''
import numpy as np
import matplotlib.pyplot as plt

#evenly sampled time at 200ms intervals
t = np.arange (0,5,.2)

#red dashes, blue square and green triangles
plt.plot (t, t, 'r--',t**2, 'bs' , t, t**3, 'g^')

plt.show()
'''
'''
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-10,10,1)
plt.plot(x,x**2,'rs')

plt.axis([-10,10,0,36])
plt.grid(True)
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

def f(t):
	return np.exp(-t)*np.cos(2*np.pi*t)

t1=np.arange(0.0 , 5.0 , 0.1 )
t2=np.arange(0.0 , 5.0 , 0.2 )

plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1),'rx',t2,f(t2))

plt.subplot(212)
plt.plot(t2,f(t2),'bo')
plt.grid(True)
plt.show()


