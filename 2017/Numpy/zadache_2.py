
# -*- coding:utf-8 -*-

import numpy as np

a = np.loadtxt("file.txt", delimiter=',')
print a
#b = np.genfromtxt("file.txt",delimiter=',')
#print b

b = np.sum(a)
print b
mab= np.min(a)
mxb = np.max(a)

print mab
print mxb

