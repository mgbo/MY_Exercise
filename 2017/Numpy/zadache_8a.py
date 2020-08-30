
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[1,2],[2,5]])
print ("Matrices A is : ")
print (A)

B = np.array([[4,-6],[2,1]])
print ("Matrices B is : ")
print (B)

A_d = det(A)
print ("Determinant of Matrices A is : ")
print (A_d)

x = solve(A,B)
print ("Ответ : ")
print (x)

x = np.allclose(np.dot(A,x),B) # для проверка
print (x)
