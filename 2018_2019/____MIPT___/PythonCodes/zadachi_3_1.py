
'''
Задача 3.1: буквы в числа
Дан текст. Замените каждую букву на число - порядковый номер буквы в алфавите. А на 1, В на 2, С на 3 и так далее.

Пробел заменять на 0. Другие символы оставлять как есть.

Числа печатайте через пробел.

Input	Output
hello	8 5 12 12 15
Hello, world!	8 5 12 12 15 , 0 23 15 18 12 4

'''
import string

text = input()
text = text.lower()
 
oldalphabet = string.ascii_lowercase 
# print(oldalphabet)
# oldalphabet = 'abc'

def make_kodiyabaniye(oldalphabet, text):
	my_code = ''

	for l in text:
		for i,cc in enumerate (oldalphabet):
			if l == cc:
				# print (i+1, end=' ')
				my_code += str(i+1) + ' '
				
		if l not in oldalphabet:
			my_code += l

		if l == ' ':
			my_code += str(0) + ' '

	return my_code


ans = make_kodiyabaniye(oldalphabet, text)
print (ans)





