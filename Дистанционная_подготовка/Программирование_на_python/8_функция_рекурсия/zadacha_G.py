

a = float(input())
n = int(input())

def power(a, n):
	if n == 0:
		return 1

	if n>= 1:
		print ("{} {} = {}".format(a, power(a, n-1), a*power(a, n-1)))
		return a * power(a, n-1)

ans = power(a, n)
print ("{:0.0f}".format(ans))