
## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'bannana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]


print (afruits)## ['APPLE', 'BANNANA']

print ("----------")
for s in fruits:
	if 'a' in s:
		print (s)
	#print (s)