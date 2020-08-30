
# map() - применить функцию ко всем элементам списка

a = map(int, input().split()) # ввели эти числа
print (a) # map - это не список


b = list(a) # но из map можно получить list
print (b)


############## пример- квадраты чисел #####################

'''

map(function_to_apply, list_of_inputs)

'''
n = [1,2,3,4,5]

squared = map((lambda x: x**2), n) # map - это не список

print (squared)

b = list(squared) # но из map можно получить list
print (b)



###########################################################

def multiply(x):
	return (x*x)

def add(x):
	return (x+x)

funcs = [multiply, add]

#for i in range(5):
#	print (funcs)

for i in range(5):
	value = list(map(lambda x: x(i), funcs))
	print (value)







