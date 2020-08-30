
# -*- coding: utf-8 -*-

def perimetr(a, b):  # создали первую функцию perimetr, в нее передают два числа a и b
  res = (a+b)        # Ошибка! Забыли *2
  return res         # возвращает число

# Проверим функцию perimetr
print(perimetr(3,5)) # периметр должен быть равен 16

print (perimetr(3,5),16)


assert(perimetr(3,5)==8)

def msm(h):
    m = h//100
    sm = h % 100
    return m, sm

print(msm(157), 1, 57)      # напечатает (1 57) 1 57 - можно проверить глазами
assert(msm(157)==(1, 57))  # программа сама проверит, что msm(157) вернет 1 и 57
