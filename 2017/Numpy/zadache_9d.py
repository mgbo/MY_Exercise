
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[2,2,3],[1,-1,0],[-1,2,1]])
print "Матрица A : "
print A

A_I = inv(A)
print "Обратраная матрица A : "
print A_I