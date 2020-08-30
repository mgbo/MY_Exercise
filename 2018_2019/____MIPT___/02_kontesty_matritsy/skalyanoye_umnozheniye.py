
def scal(a, b):
	res = 0
	for i in range(len(a)):
		res = res + a[i] * b[i]
	return res

a = [3, 7, -1]
b = [2, 1, 10]
x = scal(a, b)

print (a)
print (b)
print (x)
