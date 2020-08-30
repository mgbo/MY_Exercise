
# -*- coding:utf-8 -*-

capitals = {
	'Russia': 'Moscow',
	'Ukraine': 'Kiev',
	'USA': 'Washington', 
	'Myanmar':'Naypyidaw', 
	'Mongolia':'Ulaanbaatar', 
	'China':'Beijing'
}

print capitals['Myanmar']

print "\n---------\n"

print capitals

# монжно явно написать, что по списку ключей
for s in capitals:
	print (s,capitals[s])

print "\n---------\n"

# и отсортировать ключи
for s in sorted(capitals.keys()):
	print (s,capitals[s])

print "\n---------\n"
# только значения

for c in sorted(capitals.values()):
	print (c)

print "\n---------\n"

for s,c in sorted(capitals.items()):
	print (s,c)
