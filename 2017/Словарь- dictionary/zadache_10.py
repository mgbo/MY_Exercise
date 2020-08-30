
# -*- coding:utf-8 -*-
list_pokupatel = []

f = open('bet.log','r')

for line in f:
	line = line.split()
	if not line:
		break
	pokupatel = line[1]
	list_pokupatel.append(pokupatel)

f.close()

flist_pokupatel = set(list_pokupatel)
print (flist_pokupatel)
print ("-------------")

max_pokupaka = int(input("max pokupara : "))
for n in flist_pokupatel:
	coun = list_pokupatel.count(n)
	if coun>max_pokupaka:
		print (n,coun)



