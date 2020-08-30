
import math

print (math.factorial(5))

'''
def fac(n):
	if n == 0:
		return 1
	return fac(n-1) * n
'''

"""
0 шаг. Вызов функции: fac(5)

1. fac(5) возвращает fac(4) * 5
2. fac(4) => fac(3) * 4
3. fac(3) => fac(2) * 3
4. fac(2) => fac(1) * 2
5. fac(1) => 1
6. 1 * 2 - возврат в вызов fac(2)
7. 2 * 3 - fac(3)
8. 6 * 4 - fac(4)
9. 24 * 5 – fac(5)
10. Возврат в основную ветку программы значения 120.
"""
