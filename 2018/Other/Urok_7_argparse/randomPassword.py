
import string
import random

def generatePassword(num):
	password = '' # пустая
	
	for n in range (num):
		x = random.randint(0,9)
		password +=string.printable[x]

	return password

psw = generatePassword(20)
print (psw)