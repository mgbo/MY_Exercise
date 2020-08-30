
def total(n):
	if n == 1:
		print ("n is now 1")
	else:
		print (n)
		return total(n-1)


total(10)

# Пример - 1
def get_recursive_factorial(n):
	if n < 0:
		return -1

	elif n < 2:
		return 1

	else:
		return n * get_recursive_factorial(n-1)

ans = get_recursive_factorial(4)
print (ans)