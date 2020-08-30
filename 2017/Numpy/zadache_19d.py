import numpy as np
from numpy.linalg import inv

A = np.array([[-1,0],[1,-1]])
I = inv(A)

C = np.array([[1,2],[3,4]])

prd1 =  np.dot(I,C)

B = np.array([[-1,0],[1,-1]])
I1 = inv(B)

prd2 = np.dot(prd1,I1)
print prd2

