

'''
скалярное произведение векторов
_ _    _  _     _   _       _ ^_
a b = (a, b) = |a| |b| cos (a, b)
 _	_
(a, b) = a1b1 + a2b2

 -
|a| = sqrt (a1^2 + a2^2)

'''

import math

x1, y1, x2, y2 = map(int, input().split())

sb_ab = x1 * x2 + y1 * y2

mo_a = math.sqrt (x1*x1 + y1*y1)
mo_b = math.sqrt (x2*x2 + y2*y2)

angle = sb_ab/ (mo_a * mo_b)

print ('{:.4f}'.format(angle))

