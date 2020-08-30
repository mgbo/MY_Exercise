
# -*- coding:utf-8 -*-

import numpy as np
from numpy.linalg import inv,det,solve 

# 3 * x0 + x1 = 9
# x0	 + 2 * x1 = 8

a = np.array([[3,1],[1,2]])
b = np.array([9,8])

print "A"
print a

print "B"
print b

ai = inv(a)
print ai
