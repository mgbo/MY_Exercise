import numpy as np
from numpy.linalg import inv

A = np.array([[1,3],[1,4]])
I = inv(A)

print I
