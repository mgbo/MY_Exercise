
# -*- coding:utf-8 -*-

pokupka =[]

f=open('bet.log','r')

for line in f:
	a=line.split()
	print (a)
	if not a:
		break
	t3 = a[1]
	pokupka.append(t3)

#print pokupka

print ('--------')

print ("Всего покупок в магазине : ", len(pokupka))

f.close()
