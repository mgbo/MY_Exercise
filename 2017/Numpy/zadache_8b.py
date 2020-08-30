
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[2,1],[2,1]])
print "Matrices A is : "
print A

B = np.array([[1,0],[0,1]])
print "Matrices B is : "
print B

A_d = det(A)
print "Determinant of Matrices A is : ",A_d
if A_d == 0 :
	print "нет решения"

if A_d != 0:
	x = solve(A,B)
	print "Ответ : "
	print x

	x = np.allclose(np.dot(A,x),B)
	print x




