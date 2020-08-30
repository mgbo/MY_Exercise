
# -*- coding: utf-8 -*-

x= []
y= []
interval = 60

f=open('bet_1.log','r')

line=f.readline()
a=map(int,line.split())
t=a[0]
t_start=t

i=0

while line:
	print line
	a=map(int,line.split())
	t=a[0]
	print t
	
	n=(t-t_start)/interval
	
	if n*interval in x:
		print i
		y[i-1]=y[i-1]+1
	else:
		x.append(n*interval)
		y.append(1)
		print i
		
	print x
	print y
	line=f.readline() # читаем все остальные
f.close()
