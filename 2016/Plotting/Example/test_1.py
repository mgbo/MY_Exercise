
import numpy as np
import pylab as pl

data=np.loadtxt('fakedata.txt')

pl.plot(data[:,0],data[:,1],'ro')

pl.xlabel('x')
pl.ylabel('y')
pl.grid(True)

pl.xlim(0.0,10.)

pl.show()
