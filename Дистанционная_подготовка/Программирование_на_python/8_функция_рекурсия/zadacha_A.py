
import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())


length = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))

print ('{:f}'.format(length))