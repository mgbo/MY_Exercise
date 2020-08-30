
n = list(map(int, input().split()))

def IsAscending(n):
	i = 0

	while i < len(n) -1:
		a = n[i]
		b = n[i+1]

		if a < b:
			b = a

		else:
			print ('NO')
			break
		i +=1

	else:
		print ('YES')

IsAscending(n)