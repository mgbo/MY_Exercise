
'''
	все остальные
	функция next() у любого объекта, который можно перебрать в for дает 1(очередной)
	элемент.
	прочитаем первую строку с помощью next:

'''

import sys

first = next(sys.stdin)
print ('First line is : ', first)

print ('Other lines: ')
for line in sys.stdin:
	print (line)