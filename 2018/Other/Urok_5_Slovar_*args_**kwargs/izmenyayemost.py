
'''
def add_to(num, target=[]):
	target.append(num)
	return target

add_to(1)
add_to(4)#[1, 4]

ans = add_to(5)
print (ans) # [1, 4, 5]
'''

def add_to_1(num, target=None):
	if target is None:
		target = []
	target.append(num)
	return target

print (add_to_1(1))
print (add_to_1(2))

print (add_to_1(2))







