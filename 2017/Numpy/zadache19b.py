import numpy as np
from numpy.linalg import inv,det,solve

A = np.array([[1,1,-1],[2,1,0],[1,-1,1]])
I = inv(A)

D = det(A)

B = np.array([[1,-1,3],[4,3,2]])
S = np.dot(B,I)
print S
