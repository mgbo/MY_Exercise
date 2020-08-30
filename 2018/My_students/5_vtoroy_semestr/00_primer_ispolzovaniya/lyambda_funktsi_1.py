
# Пусть у нас есть список кортежей, которые описывают химические элементы (нормер группы, порядковый номер, название)
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]
print (elements)

# при сортировке по умолчанию получим,
ans = sorted(elements)
print (ans)

elements.sort(key=lambda e:(e[1], e[2]))
print (elements)

# по другому
elements.sort(key= lambda e: e[1:3])
print (elements)