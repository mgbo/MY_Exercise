
alpha = 'abcdefghijklmnopqrstuvwxyz'
#print (type(alpha))
#print (len(alpha))
# print (alpha)

# test index
i_b = alpha.index('b')
# print (i_b)

code = ''
for letter in alpha:
	code += alpha[(alpha.index(letter) + 3)%len(alpha)]

# print (code)
# print ("-----------")


l = input()
mycode = ''
space = ' '

for letter in l:
	if letter != space:
		mycode += alpha[(alpha.index(letter.lower()) + 3) % len(alpha)]

	elif letter == space:
		mycode += letter

print (mycode)

