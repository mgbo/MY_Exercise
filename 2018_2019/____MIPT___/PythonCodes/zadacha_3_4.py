
'''
Задача 3.4: Оставить только НЕ гласные буквы
В английском алфавите буквы eyuioa - гласные. 
Удалите из текста все гласные буквы. Удалите из текста все НЕ буквы.
'''
import string
text = input()
text = text.lower()
# alphabet = string.ascii_lowercase 
alphabet = 'bcdfghjklmnpqrstvwxz'

vowels = 'aeiouy'

def remove_vowels(vowels, text):
	ans = ''
	for t in text:
		if t not in vowels and t in alphabet:
			ans += t

	return ans

res = remove_vowels(vowels, text)
print (res)






