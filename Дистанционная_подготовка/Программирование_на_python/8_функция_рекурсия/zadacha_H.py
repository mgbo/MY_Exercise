
n = int(input())
m = int(input())

def GCD(n, m):
	while n!= 0 and m!=0:
		if n > m:
			# print ("n > m --> ", n, m, n%m)
			n %= m
		else:
			# print ("n < m --> ", n, m, m%n)
			m %= n
	return n+m


def ReduceFraction(n, m):
	gcd = GCD(n, m)
	return n//gcd , m//gcd

ans = ReduceFraction(n, m)
print (*ans)