# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sys import exit

klient=[]
kolichebo={}

f=open('bet_1.log','r')
g=f.read().split('\n')
f.close()

for line in g:
	a=map(int,line.split())
	print a
	if not a:
		break
	klient.append(a[1])

print klient	
#~ exit(0)

uniq_klient = set(klient)
for k in uniq_klient :
	kolichebo[k] = klient.count(k)

print "klient : ",klient
print "kolichebo: ",kolichebo

numkolichebo=len(kolichebo)
print "klichebo : ",numkolichebo

x = []
y = []

for k, v in kolichebo.items() :
	x.append(k)
	y.append(v)

plt.bar(x, y, color='b')

plt.title ('GRAPPIC')
plt.xlabel('kolichebo')
plt.ylabel('klient')
plt.grid (True)
plt.show()


