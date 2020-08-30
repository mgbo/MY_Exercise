
#-*- coding:utf-8 -*-
nomer = []

with (open ('bet.log','r')) as f:
	for line in f:
		s = line.split()
		if not s:
			break
		pokypatel = s[1]
		nomer.append(pokypatel)

d = {}
for i in nomer:
	d[i]=d.get(i,0)+1

for k,v in d.items():
	print (k,v)
