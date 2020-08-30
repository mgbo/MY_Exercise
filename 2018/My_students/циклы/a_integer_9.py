
def function(x):
	y = (2*(x**2)) + 16
	return y

a,b = map(int,input().split())

delta = 0.025

n = (b-a)/delta # количество шагов

x = a # сначало x равен началу отрезка + delta

'''
начинаем с нулевого шага i==0
пока i>n вычисляем значения функции и печетаем
'''

i = 0
ploshchad =0

while (i<n):

	middle = x + delta/2 # вычислили середину шага

	y = function(middle) # вычислили значение в точке x

	area = y*delta # area

	ploshchad+= area

	print ("i = {} , x = {} , middle = {} , y = {} , площадь = {} ".format(i,x,middle,y,ploshchad))
	
	x = x + delta # изменили x на delta

	i+=1 # увеличили номер шага







