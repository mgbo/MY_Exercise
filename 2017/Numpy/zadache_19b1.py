import numpy as np
from numpy.linalg import inv

A = np.array([[1,1,-1],[2,1,0],[1,-1,1]])
I = inv(A)
print I
B = np.array([[1],[2],[3]])
print B
X = np.dot(I,B)

print X

