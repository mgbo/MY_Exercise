
foo = ['hi']

print (foo) # ['hi']

bar = foo

bar +=['bye']

print (foo) # ['hi', 'bye']

"""
def add_to(num, target=[]):
	target.append(num)
	return target

add_to(1)
add_to(2)
print (add_to(3))
"""

def add_to(element, target=None):
	if target is None:
		target = []
	target.append(element)
	return target

# Каждый раз при вызове функции без аргумента target будет создан новый список.
# К примеру:

print(add_to(54))
print (add_to(88))









