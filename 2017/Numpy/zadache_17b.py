import numpy as np
from numpy.linalg import inv

A = np.array([[1,2,-4],[0,0.5,3],[0,0,2]])
I = inv(A)

print I
