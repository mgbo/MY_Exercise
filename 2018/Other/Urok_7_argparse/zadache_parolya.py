
import random


'''
str_1 = input("буковок : ")
print ("str_1 : ",str_1)

str_2 = input("циферок : ")
print ("str_2 : ",str_2)

str_l = str_1 + str_2 + str_1.upper() + str_2.upper()

print ("str_l : ",str_l) 
'''
str_1 = 'dlfjld'
str_2 = '34343'
str_l = str_1 + str_2 + str_1.upper() + str_2.upper()
print (str_l)

def generateP(str_l):
	p = '' # пустая
	for n in str_l:
		#print (n)
		p+=random.choice(n)
		
	return p

psw = generateP(str_l)
print (psw)

