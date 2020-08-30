
#-*- coding:utf-8 -*-
A = dict()

with (open('strana_yazyki.txt','r')) as f:
	for line in f:
		words = line.split(':')
		coun = words[0]
		lang = words[1]
		A[coun]=lang
f.close()

Lcou =[]
N = int(input('Number of country :'))
for i in range(N):
	nam_coun = input()
	Lcou.append(nam_coun)
	for k,v in A.items():
		if Lcou[i] in k:
			print(v)
