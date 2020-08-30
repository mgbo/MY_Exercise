

# Урок 2
# Функция get

'''
В python уже есть такая функция dict.get(key, default_value=None).

	Если в словаре есть такой ключ, то функция вернет dict[key].
	Если в словаре такого ключа НЕТ, то вернет default_value.
	Если нет default_value, вернет None.
'''

dcolors = {
	'a': 'blue',
	'b': 'red',
	'c': 'green',
	'd': 'gold',
	'v': 'violet',
	'o': 'orange',
	'z': 'yellow'
}

for k,v in dcolors.items():
	print (k,v)

col = dcolors.get('z', 'gray') # yellow, если есть ключ z
print (col)

col = dcolors.get('www', 'gray') # gray, нет ключа www значение по умолчанию gray











