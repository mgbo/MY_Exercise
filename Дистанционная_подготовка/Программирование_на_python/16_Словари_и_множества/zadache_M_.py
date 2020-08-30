
import sys

d = {}

def func(key, val):
    if key in d:
        d[key] += int(val)
    else:
        d[key] = int(val)

for w in sys.stdin:
	k,v = w.split()
	func(k,v)

print ("------------")

l = d.keys() # получаем ключи
print (l)
l = list(l) # превращаем его в обычный список
print (l)

l.sort() # сортируем список
for i in l: # вывод элементов словаря по алфавиту
    print(i, d[i])
