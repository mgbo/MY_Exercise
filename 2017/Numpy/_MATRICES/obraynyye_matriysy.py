
# -*- coding:utf-8 -*-
import numpy as np
from numpy.linalg import inv,det,solve

# AB=BA=I

A = np.array([[1,3],[1,2]])

print "Matrices A is "
print A

print "Inverse A is "
Ai = inv(A)
print Ai

print "A*Ai is : "
print (np.dot(A,Ai))
