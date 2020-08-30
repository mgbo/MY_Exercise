
def generator_function():
	for i in range(10):
		yield i

for item in generator_function():
	print (item)

print ("---------")

gen = generator_function()
print (next(gen)) # 0

g = generator_function

for item in g():
	print (item)