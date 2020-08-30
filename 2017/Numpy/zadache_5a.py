
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

# AB, BA, A^T B^T , B^T A^T

A = np.array([[0,1],[1,0]])
print (A)

B = np.array([[0,0],[1,0]])
print (B)

AB = A.dot(B)
print ("\nAB\n")
print (AB)

BA = B.dot(A)
print ("\nBA\n")
print (BA)

A_T = (A.T)
B_T = (B.T)

A_T1 = A_T.dot(B_T)
print ("\nA_T*B_T\n")
print (A_T1)

A_T2 = B_T.dot(A_T)
print ("\nB_T*B_T\n")
print (A_T2)
