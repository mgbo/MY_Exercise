
'''
Сумма двух квадратов
'''

n = int(input())

def square(n):
	return n*n

for i in range(1, 20):
	x1 = square(i)

	if x1 > n:
		break

	for j in range(1, 20):
		value = x1 + square(j)

		if value == n:
			print (i,j)

		elif value > n:
			print ('Imposible')
			break
