
# -*- coding:utf-8 -*-

import numpy as np
import numpy.linalg as lg

A = np.array([[3,1],[1,2]])

print "Matrices A :"
print A

print "Determinant of A"
print (lg.det(A))

B = np.array([9,8])
print "Matrices B :"
print B

A_I = lg.inv(A)
print A_I

ans = np.dot(A_I,B)
print "ans"
print ans

print "\n------- ПО ДРУГОМУ -----\n"
ans_1 = lg.solve(A,B)
print ans_1

AA = np.array([[1,1,-1],[2,1,0],[1,-1,1]])

print AA

print "Dat A\n"
D_A = lg.det(AA)

print "Tran AA"
T_A = AA.T
print T_A


anss = T_A/D_A

print anss


