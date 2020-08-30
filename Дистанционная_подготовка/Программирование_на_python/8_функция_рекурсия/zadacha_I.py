
n = int(input())


def MinDivisor(n):
	i = 1
	while i<= n:
		i +=1
		if n % i == 0:
			break

	return i

ans = MinDivisor(n)
print (ans)
