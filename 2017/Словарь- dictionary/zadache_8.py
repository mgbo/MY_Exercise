
# -*- coding:utf-8 -*-

# сколько разных клиентов ?

a=[]
pokupatel = []
f = open ('bet.log','r')

for line in f:
	a = line.split()
	#print a
	if not a:
		break
	t1 = a[1]
	pokupatel.append(t1)
print ("-----------")
print ("len ",len(pokupatel))

raznyy_pokupatel = set(pokupatel)
print ("\n-----------\n")
print (raznyy_pokupatel)


raznyy = {} # это не пустое множество, а пустой словарь!
for n in raznyy_pokupatel:
	p = pokupatel.count(n)
	raznyy[n] = p 
	print (n,p)

	



