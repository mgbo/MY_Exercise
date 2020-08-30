
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[-1,4],[8,0]])
A_I = inv(A)

nl = len(A)
print "количество строк : ", nl

nc = len(A[0])
print "количество столбцов : ", nc

if nl!=nc:
	print "Нет решения"
else:
	D_A = det(A)
	print "Determinants : ", D_A
	if D_A!=0:
		A_I = inv(A)
		print "Обратраная матрица A : "
		print A_I