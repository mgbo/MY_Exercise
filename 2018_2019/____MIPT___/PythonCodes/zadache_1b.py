
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

# print (make_alphabet(oldalphabet, 3))


def make_kodirobaniye(oldalphabet, newalphabet, text):
	ans = ''
	print ("NewAlphabet :\t ",newalphabet)
	for i in text:
		if i in oldalphabet:
			ans += newalphabet[(newalphabet.index(i) + 3)%len(oldalphabet)]
		else:
			ans += i

	return ans



newalphabet = make_alphabet(oldalphabet, n)
# print (newalphabet)  # Новый алфавит

codetext = make_kodirobaniye(oldalphabet, newalphabet, text)
print (codetext)
















