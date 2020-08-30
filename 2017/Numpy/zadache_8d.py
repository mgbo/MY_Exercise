
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[2,1],[3,2]])
print "Matrices A is : "
print A

A_i = inv(A)
print "Inverse Matrices A is "
print A_i

E = np.dot(A_i,A)
print "Identity Matrices "
print E

B = np.array([[-3,2],[5,-3]])
print "Matrices B is : "
print B

C = np.array([[-2,4],[3,-1]])
print "Matrices B is : "
print C

X = np.dot(A_i,C)

I_1 = inv(B)
ans = np.dot(X,I_1)
print "poslednoye resheniye"
print ans


