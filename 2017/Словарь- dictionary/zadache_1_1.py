
# -*- coding: utf-8 -*-

nn = input()
print ("nn : ", nn)

without_sp = list(map(int,nn.split()))
print (without_sp)
print (type(without_sp))

sl=set(without_sp)

print('----')
print (sl)

for n in set(without_sp):
	p=without_sp.count(n)
	print (n,p)
