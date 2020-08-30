
'''
# будем читать много целых чисел через пробел
m = map(int, input().split())

# берем по 1 числу, читаем число в х
for x in m:
	print(x)    # печатаем 1 число

# этот цикл ничего печатать не будет. 
# Мы уже прочли числа. Второй раз их читать нельзя. 
for x in m:
	print(x)

'''

import turtle

t = turtle.Turtle()

m = map(int, input().split())

def w(n):
	t.write((n), font=("Arial", 14, "normal"))

i = 0

for x in m:
	t.fd(x)
	i+=x
	w(i)

turtle.done()



