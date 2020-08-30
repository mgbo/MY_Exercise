
# -*- coding:utf-8 -*-

vremya =[]

f=open('bet.log','r')

for line in f:
	a=list(map(int,line.split()))
	if not a:
		break
	t = a[0]
	vremya.append(t)
f.close()
print ('--------')

t_0 = vremya[0]
t_final = vremya[-1]

print (t_0)
print (t_final)

vremya_sekunda = t_final - t_0
print ("время в секунда {} sec ".format(vremya_sekunda))

vremya_minuta = vremya_sekunda/60
print ("время в минута {} min ".format(vremya_minuta))

vremya_chasov = vremya_minuta/60
print ("время в часов  {} hour ".format(vremya_chasov))







