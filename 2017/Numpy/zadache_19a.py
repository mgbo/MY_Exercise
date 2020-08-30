import numpy as np
from numpy.linalg import inv,solve

A = np.array([[1,3],[1,4]])
I = inv(A)
B = np.array([[1,-1],[-1,1]])

X = np.dot(I,B)

print X
