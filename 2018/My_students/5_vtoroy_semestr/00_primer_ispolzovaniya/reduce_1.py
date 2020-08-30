
'''
	reduct(funtion_to_apply, list_of_inputs, init_value)
'''

product = 1
list = [1,2,3,4,5]

for num in list:
	product = product * num

print (product)

# c reduct

from functools import reduce

product = reduce((lambda res, x : res*x), [1,2,3,4,5],1)
print (product)