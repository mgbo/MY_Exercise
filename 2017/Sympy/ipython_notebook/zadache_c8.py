
#-*- coding:utf-8 -*-

from sympy import*

A = Matrix([[1,2],[2,5]])
pprint (A)

B = Matrix([[4,-6],[2,1]])
pprint (B)

A_i = A.inv()
pprint (A_i)

pprint(A*A_i)

x = A_i*B

pprint(x)

