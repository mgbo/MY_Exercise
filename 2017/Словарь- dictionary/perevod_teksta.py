
#-*- coding:utf-8 -*-

A = dict()
with (open('slovar.txt','r')) as f:
	for line in f:
		words = line.split('-')
		coun = words[0]
		lang = words[1:]
		A[coun]=lang
f.close()

f_2 = open('tesk.txt','r')

nn = input()
for k,v in A.items():
	if nn in k:
		print (v)
LL= []
for i in f_2:
	w = i.split()
	LL.append(w)

print(LL)