
def foo(x):
	return x*x

a = [2, 5, 3, 7]
b = map(foo, a)
b = list(b)
print(b)

print(a)
for x in b:
	print(x, end='-')

print ("\n")