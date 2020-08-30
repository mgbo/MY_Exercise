
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


ug=[]
kolichestbo=[]
time=[]
t_start=0
interval=1



action='login'
f=open('tr.log','r')

g=f.read().split('\n')
f.close

for line in g:
	a=map(str,line.split())
	#print 'File a is : ',a
	if not a:
		break
	
	if t_start==0:
		t_start=int(a[0])
	if action==a[2]:
		time.append((int(a[0])-t_start)/interval)
		print "Action : ",action
		kolichestbo.append(1)
	

print "Time : ",time
print "Period : ",kolichestbo


plt.plot(time,kolichestbo,'ro')

plt.title('Graphic')
plt.xlabel('Time')
plt.ylabel('kolichesto')

plt.grid(True)
plt.show()

	

