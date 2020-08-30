
'''
Задача 3.2: Обратная задача
Замените числа, написанные через пробел, на буквы. Не числа не изменять.

Input	Output
8 5 12 12 15	hello
8 5 12 12 15 , 0 23 15 18 12 4 !	hello, world!
'''

import string


text = list(map(str, input().split()))
oldalphabet = string.ascii_lowercase 
print(oldalphabet)


def make_kodiyabaniye(oldalphabet, text):
	my_code = ''

	for l in text:
		for i,cc in enumerate (oldalphabet):
			if l == str(i+1):
				# print (i+1, end=' ')
				my_code += cc + ''

		if l in ',.!':
			my_code += l

	print (my_code)

make_kodiyabaniye(oldalphabet, text)













