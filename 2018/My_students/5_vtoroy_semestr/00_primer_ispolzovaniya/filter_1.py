
'''
	filter(filter_function, list_of_inputs)
'''

numbers = range(-5,5)
print (numbers)
print (list(numbers))

less_than_zero = list(filter(lambda x: x<0, numbers))
print (less_than_zero)

# filter похож на цикл, но он является встроенной функцией и работает быстрее
