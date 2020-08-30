# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sys import exit
import matplotlib.pyplot as plt


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
print "uniq_klient : ",uniq_klient


for k in uniq_klient :
	kolichebo[k] = klient.count(k)

#print "klient : ",klient
print "kolichebo: ",kolichebo

numkolichebo=len(kolichebo)
print "klichebo : ",numkolichebo

x = []
y = []

for k, v in kolichebo.items() :
	x.append(k)
	y.append(v)

print "номер клиента (y) : ",y
print "количество покупки для одного клиента (x) : ",x


#objects=('mg mg','mg kyaw','mg chit','ma nge','ma mya')
#x_pos=np.arange(len(objects))

plt.bar(x, y,align='center',alpha=1, color='g')

plt.title ('GRAPPIC')
plt.xlabel('klient')
plt.ylabel('klichebo')
plt.grid (True)

plt.show()


