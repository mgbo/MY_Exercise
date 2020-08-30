

alpha = 'abcdefghijklmnopqrstuvwxyz'
#print (type(alpha))
#print (len(alpha))

'''
code = ''

for letter in alpha:
	code += alpha[(alpha.index(letter) + 3)%len(alpha)]


print (code)


print ("-----------")
'''


l = input()
mycode = ''
space = ' '

for letter in l:
	if letter!= space:
		mycode+= alpha[(alpha.index(letter) + 3)%len(alpha)]
	elif letter == space:
		mycode+=space


print (mycode)


