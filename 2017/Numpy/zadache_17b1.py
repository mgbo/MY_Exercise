import numpy as np
from numpy.linalg import inv

A = np.array([[1,1,1.5],[1,-1,0],[-2,4,2]])
I = inv(A)

print I

