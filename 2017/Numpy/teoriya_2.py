
# -*- coding:utf-8 -*-

import numpy as np
import numpy.linalg as lg

def f(n,m):
	res = n + 10*m
	return res

A = np.fromfunction(f,(6,6),dtype=int)

print A

print A[:3,:3]
print A[::2,::2]