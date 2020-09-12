
# ------ method-1 -----------
#########################
def square_number(nums):
	result = []

	for i in nums:
		result.append(i*i)

	return result

# my_number = square_number ([1,2,3,4,5])
# print (my_number)



#--------- method-2 -----------
################################
# my_number = [i*i for i in [1,2,3,4,5]]
# print(my_number)


# -------- Generator ------------
################################
def square_number(nums):
	for i in nums:
		yield (i*i)

'''
Generator is better with performance because it is not holding all the values in memory
'''

# yield method don't hold the entire result in memory and it yields one result at a time
my_number = square_number ([1,2,3,4,5])
print (my_number)
print (next(my_number))
print (next(my_number))

for i in my_number:
	print (i)

# generator
my_number = (x*x for x in [1,2,3,4,5]) # this is generator
print (my_number)
print (list(my_number))

for i in my_number:
	print (i)

