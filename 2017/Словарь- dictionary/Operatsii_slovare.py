
# -*- coding:utf-8 -*-
A = {
    'Russia': 'Moscow', 
    'Ukraine': 'Kiev', 
    'USA': 'Washington', 
    'Myanmar':'Naypyidaw', 
    'Mongolia':'Ulaanbaatar', 
    'China':'Beijing'
}
for k,v in A.items():
	print (k,v)
print " --------------- "
print len(A)
print " --------------- "
print (A.keys())

print " --------------- "
value = A['China']
print value

# Получение элемента по ключу 
# Если элемента в словаре нет,то get возвращает None
value_1 = A.get('mm')
print value_1

value_2 = A.get('Myanmar')
print value_2

value_3 = A.get('Chit',-8)
print value_3

proverka = 'USA' in A # Проверить принадлежность ключа словарю
print proverka

proverka_1 = 'chit' not in A
print proverka_1

A['India'] = 'NewDeli'
for k,v in A.items():
	print (k,v)

print "--------------------"

del A['India']
for k,v in A.items():
	print (k,v)	

if 'China' in A:
	del A['China']

print "--------------------"
for k,v in A.items():
	print (k,v)	


val = A.pop('USA') # удаление пары ключ-значение
print val
print "--------------------"
for k,v in A.items():
	print (k,v)	

val_1 = A.pop('Uka',-2)
print val_1 







