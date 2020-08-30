
'''

Задача 2. Взлом шифра
Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
Попробуйте все возможные сдвиги и расшифруйте фразу.

Номер варианта дает преподаватель

'''
text = input()
text = text.lower()

oldalphabet = 'abcdefghijkmnopqrstuvwxyz'

def make_dekodirobaniye(oldalphabet, text, n):
	de_code = ''
	for i in text:
		if i in oldalphabet:
			de_code += oldalphabet[(oldalphabet.index(i)+ (25+n))%len(oldalphabet)]
		else:
			de_code += i

	return de_code


n = 1
while n!= 0:
	codetext = make_dekodirobaniye(oldalphabet, text, n)
	print (codetext)
	n = int(input("Введите сдвиг : "))
	
	



