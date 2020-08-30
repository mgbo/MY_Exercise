
# -*- coding:utf-8 -*-

import numpy as np
import numpy.linalg as lg

a = np.array([[2,1,3],[2,3,4]])
print "Matrices A "
print (a)

s = a.shape
print "размерность массива : ",s

print "количество строк : ", len(a)
print "количество столбцов : ",len(a[0])

print "количество элементов : ", a.size
print (a.ndim)