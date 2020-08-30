
# -*- coding:utf-8 -*-

capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}

# монжно явно написать, что по списку ключей
for s in capitals:
	print (s,capitals[s])

print ("\n--------\n")

list2 = []

n = int(input("Number of city : "))
for j in range(n):
    city = input()
    list2.append(city)

    for key, value in capitals.items():
        if list2[j] in value:
            print ("MY country is ",key)

'''
print "\n--------\n"

# и отсортировать ключи
for s in capitals.keys():
	print (s)

print "\n--------\n"

# и отсортировать значение
for s in capitals.values():
	print (s)
'''
