# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[1,1,-1],[2,1,0],[1,-1,1]])
print "\nMatrices A is :\n "
print A

B = np.array([[1,-1,3],[4,3,2],[1,-2,5]])
print "\nMatrices B is : \n"
print B

A_I = inv(A)
print "A_I"
print A_I

#print (np.dot(A_I,A)) # Внимание

X = np.dot(B,A_I)
print "poslednoye resheniye"
print X

'''
XX =X.astype(int)
print XX
'''
