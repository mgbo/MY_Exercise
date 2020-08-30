
# -*- coding:utf-8 -*-

import numpy as np
import numpy.linalg as lg 

A = np.array([[1,2,3],[4,5,6]])
print "Matrices A is : "
print A


B = np.array([[23,45,23],[34,45,67]])
print "Matrices B is : "
print B

A = np.savetxt("my_save.txt",A,delimiter=" ")
B = np.savetxt("my_save.txt",B,delimiter=" ")
