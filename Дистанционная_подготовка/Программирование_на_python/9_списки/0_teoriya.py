
A = ['red', 'green', 'blue']

print (' '.join(map(str, A)))

print('*'.join(A))


A = [ input() for i in range(int(input()))]
print (A)

import random

B = [random.randint(1, 9) for i in range(10)]
print (B)