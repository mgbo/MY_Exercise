
'''
Задача 1
Написать одному чесловеку кодирование (шифрование), а другому - декодирование (расшифровку)

'''

n = int(input())
text = input()
text = text.lower()
# print (text)

oldalphabet = 'abcdefghijkmnopqrstuvwxyz'

# или можно написать так:
# oldalphabet = string.ascii_lowercase 

def make_alphabet(oldalphabet, n):
	new = ''
	for l in oldalphabet:
		new +=oldalphabet[(oldalphabet.index(l) + n) % len(oldalphabet)]

	return new

def make_kodirobaniye(oldalphabet, newalphabet, text):
	ans = ''
	# print ("NewAlphabet :\t ",newalphabet)
	for i in text:
		if i in oldalphabet:
			ans += newalphabet[(newalphabet.index(i) + 3)%len(oldalphabet)]
		else:
			ans += i

	return ans

def make_dekodirobaniye(oldalphabet, newalphabet, text):
	de_code = ''
	for i in text:
		if i in oldalphabet:
			de_code += newalphabet[(newalphabet.index(i)+ (25+nn))%len(oldalphabet)]
		else:
			de_code += i

	return de_code

newalphabet = make_alphabet(oldalphabet, n)
# print (newalphabet)  # Новый алфавит

codetext = make_kodirobaniye(oldalphabet, newalphabet, text)
print ("Кодирование :",codetext)


nn = int(input('Сдвид \t'))

print ("\nДля Декодирование")

ans_2 = make_dekodirobaniye(oldalphabet, newalphabet, codetext)
print (ans_2)







