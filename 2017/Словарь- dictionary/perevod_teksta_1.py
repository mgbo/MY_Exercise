
#-*- coding:utf-8 -*-

D = dict()
with (open('slovar.txt','r')) as f:
	for line in f:
		words = line.strip().split(':')
		if not words:
			break
		en = words[0]
		ru = words[1].strip()
		D[en] = ru
f.close()

ff = open('tesk.txt','r')
for ii in range(3):
	for i in ff:
		ss = i.split()
		print (ss[ii])







