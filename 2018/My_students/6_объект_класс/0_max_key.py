

"""
example using max function with key
"""
l = ['23','45','67','88','12','56','78','19']

print(l)

def last(n):
	return str(n[1])

print (max(l,key=last))

# example сыллка

a = [1,2,3]
print (a,id(a))

b = [1,2,3]
print (b,id(b))

print ("---------------")
a=b
print (b,id(b))
print (a,id(a))

a+=[1]
print (b)




















