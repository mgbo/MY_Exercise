
def function(x):
	y = (2*(x**2)) + 16
	return y

a,b = map(int,input().split())

delta = 2.0

# количество шагов
n = (b-a)/delta

# сначало x равен началу отрезка + delta
x = a

'''
начинаем с нулевого шага i==0
пока i>n вычисляем значения функции и печетаем
'''

i = 0


while (i<n):

	# вычислили середину шага
	middle = x + delta/2

	# вычислили значение в точке x
	y = function(middle)

	print ("i = {} , x = {} , middle = {} , y = {} ".format(i,x,middle,y))

	# изменили x на delta
	x = x + delta

	# увеличили номер шага
	i+=1







