
'''

capitals = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}

k = capitals.keys()
print (k)

v = capitals.values()
print (v)


print (capitals['Russia'])

print (capitals.get('Myanma',0))
print (capitals)

'''

#####################################################################
"""
# Создадим пустой словать Capitals
Capitals = dict()

# Заполним его несколькими значениями
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'

# Считаем название страны
print('В какой стране вы живете?')
country = input()

# Проверим, есть ли такая страна в словаре Capitals
if country in Capitals:
    # Если есть - выведем ее столицу
    print('Столица вашей страны', Capitals[country])
else:
    # Запросим название столицы и добавим его в словарь
    print('Как называется столица вашей страны?')
    city = input()
    Capitals[country] = city
"""

####################################################
users = {
    "+11111111": "Tom",
    "+33333333": "Bob",
    "+55555555": "Alice"
}

users["+4444444"] = "Sam"

'''
Но если мы попробуем получить значение с ключом, которого нет в словаре,
то Python сгенерирует ошибку KeyError:

#user = users["+4444444"]    # KeyError
'''

key = "+4444444"
if key in users:
    user = users[key]
    print(user)
else:
    print("Элемент не найден")





