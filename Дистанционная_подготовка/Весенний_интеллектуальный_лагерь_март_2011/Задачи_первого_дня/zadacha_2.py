
n = int(input())


def skolko_sekund(n):
	c = n % 60
	m = (n // 60) % 60
	h = n // 3600
	return h,m,c


print (*(skolko_sekund(n)))