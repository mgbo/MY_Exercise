
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[0,1],[1,0]])
print "Matrices A is : "
print A

A_i = inv(A)
print "Inverse Matrices A is "
print A_i

B = np.array([[5,2],[0,6]])
print "Matrices B is : "
print B

C = np.array([[0,0],[0,1]])
print "Matrices B is : "
print C

X = np.dot(A_i,C)

I_1 = inv(B)
ans = np.dot(X,I_1)
print "poslednoye resheniye"
print ans


