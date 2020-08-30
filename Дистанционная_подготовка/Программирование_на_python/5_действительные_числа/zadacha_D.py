
'''
Площадь треугольника
'''

import math

a = int(input())
b = int(input())
c = int(input())

p = a + b + c

s = p/2

A = math.sqrt(s*(s - a) * (s - b)* (s - c))

print (A)