
"""
	пример использования комманды для множеств

"""

a = [1,2,3,4,5,6,7,8,9]
b = [1,2,3,4,5,6,7,5,9,10,15]


aa = set(a)
bb = set(b)

print (aa|bb) # объединение множеств

print (aa&bb) # пересечение множеств

print (bb-aa) # вычитание

cc = a.copy() # копия множества
print (cc)

aa.add(100) # добавить 7 в множество aa
print (cc)

