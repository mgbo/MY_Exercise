
# -*- coding: utf-8 -*-

def height(h):        # функция height, в нее передают одно число h
   m = h // 100       # подсчитали рост в метрах
   sm = h % 100       # подсчитали рост в сантиметрах
   return m, sm       # вернули сразу метры и сантиметры

# дальше программа. Пользуемся функцией height и проверяем ее.
                          # мой рост 169 см. Посчитаем его в метрах и сантиметрах
mym, mysm = height(169)   # результаты функции поместили в переменные mym и mysm 
print("мой рост %d метров %d сантиметров" % (mym, mysm))

you = int(input())        # прочитали ваш рост
ym, ysm = height(you)     # результаты функции поместили в переменные ym и ysm 
print("ваш рост %d метров %d сантиметров" % (ym, ysm))
