
some_list = [1,2,3,4,5,1,2]

'''
duplicates = []

for value in some_list:
	if some_list.count(value)>1:
		if value not in duplicates:
			duplicates.append(value)

print (duplicates) #[1,2]
'''

new = []

for value in some_list:
	if some_list.count(value)>=1:
		if value not in new:
			new.append(value)

print (new)




