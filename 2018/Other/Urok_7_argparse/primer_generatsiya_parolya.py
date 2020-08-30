
import random

# щепотка цифр
str_1 = '123456789'
print ("str_1 : ",str_1,'\n')

# щепотка строчных буркв
str_2 = 'qwjdfljdloeuoldfkhkldfl'
print ("str_2 : ",str_2,'\n')

# щепотка прописных букв. Готовиться преобразованием str_2 в верхний регистр
str_3 = str_2.upper()
print ("str_3 : ",str_3,'\n')

# Соединяем все строки в одну
str_4 = str_1 + str_2 + str_3 
print ("str_4 : ",str_4,'\n')

#Преобразуем получившуюся строку в список
ls = list(str_4)

# Тщательно перемешиваем список
random.shuffle(ls)

#извлекаем из списка 12 произвольных значений
psw = ''.join([random.choice(ls) for x in range(12)])

#Пароль готов
print (psw)





