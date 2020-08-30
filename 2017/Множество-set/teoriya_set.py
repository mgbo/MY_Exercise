
# -*- coding: utf-8 -*-

a = [1,5,17,5,-22,4,4,4] # сделали list
print (a)

b =set(a) # сделали set из list
print (b)

c = {1,5,17,5,-22,4,4,4} # сделали set
print (c)

d = {} #это не set, это dict
print (d)

a = {1, 3, 5, 11, 12, 13}
b = {5, 1, 3, 21, 22, 23}
c = {1, 3, 5}
d = {3, 1, 5}
w = {2, 8}

print (len(a))
print (5  in c)
print (5 not in c)
print (a.isdisjoint(w)) # True, если у множеств нет общих элементов
print (c==d)
print (w==d)

aa = a.copy()
print (aa)

aa.remove(5)
print (aa)
