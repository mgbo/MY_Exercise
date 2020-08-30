
# -*- coding:utf-8 -*-
f=open('bet_3_2.log','r')
b=[]

line = f.readline()
a= line.split()
t0=a[0]

print ("first time = ",t0)
while line:
	line = f.readline()
	a= line.split()
	if not a:
		break
	t=a[0]
	b.append(t)
#print (b)

f.close()

print ('last time = ',t)

ans=int(t) - int(t0)
print (ans)
