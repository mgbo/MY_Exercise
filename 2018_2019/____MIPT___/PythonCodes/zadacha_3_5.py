
'''
Задача 3.5: Убрать повторяющиеся буквы и лишние символы
Построим по ключевой фразе часть алфавита. Возьмем все буквы по одному разу. Не буквы убрать.

Буквы должны идти в том порядке, в котором встретились в первый раз.
'''

text = input()
text = text.lower()
text = list(text)
print ("Main text\t :", text)

'''
def check_repeating(text):
	without_repeating = ''
	for l in text:
		if text.count(l) == 1:
			without_repeating +=l
		else:
			text.remove(l)
			without_repeating +=l
		
	return without_repeating


ans = check_repeating(text)
print ("without_repeating : ",ans)

'''
tes = 'abalazu'
tes = list(tes)
tes.remove('a')
print (tes)

