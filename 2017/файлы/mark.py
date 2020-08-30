
# -*- coding:utf-8 -*-

f = open('mark.txt')
suma = 0
n = 0


for i in f:
	#print ("len(i)) ",len(i))
	g = int(i[len(i)-2])
	print ('g is :',g)
	
	suma += g
	n += 1

	if g < 10:
		print(i[:-1])

print('Средний балл: %.2f' % (suma/n))

f.close()
