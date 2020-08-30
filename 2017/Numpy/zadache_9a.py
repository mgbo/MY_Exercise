
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

A = np.array([[1,2],[2,5]])
A_I = inv(A)
print "Обратраная матрица A : "
print A_I