
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve,matrix_rank

a = np.array([[1,2,3],[4,5,6]])

R_a =matrix_rank(a)
print R_a
