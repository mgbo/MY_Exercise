
# -*- coding:utf-8 -*-

import numpy as np
import numpy.linalg as lg 
# запоминаем библиотеку numpy.linalg под коротким именем lg

# Решим систему линейных уравнений 
# 3 * x0 + x1 = 9 и x0 + 2 * x1 = 8

A = np.array([[3,1],[1,2]])
B = np.array([9,8])
print "Matrices A is : "
print A

print "\nMatrices B is : "
print B

X = lg.solve(A,B)
print "X is : "
print X

print "\n------ ПО ДРУГОМУ -------\n"

A_d = lg.det(A)
print "Determinant"
print A_d

Ai = lg.inv(A)
print "Ai matrices is "
print Ai

Aii = np.dot(A,Ai)
print "A*Ai is : "
print Aii

print "ПОСЛЕДНОЕ РЕШЕНИЕ "
ans = np.dot(Ai,B)
print ans




