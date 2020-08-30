# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
time=[]
kolichestbo=[]

f=open('bet.log','r')
g=f.read().split('\n')
f.close()

t_start = 0
i = 0

for line in g:
	a=map(int,line.split())
	print (a)
	if not a:
		break

	if t_start == 0:
		t_start = a[0]
		print ("start : ",t_start)
	
	n = (a[0]-t_start)/60	# минут с начала теста
	print (i, n)
	
	if n in time :
		kolichestbo[i-1] = kolichestbo[i-1] + 1
	else :
		time.append(n)
		kolichestbo.append(1)
		i+=1
		
	print ("Time : ",time)
	print ("количество : ",kolichestbo)
	print ('---------------')

print ("Time :",time)
print ("kolichestbo:",kolichestbo)
numkolichestbo=len(kolichestbo)
print ("kolichestbo:k",numkolichestbo)

plt.bar(time,kolichestbo,align='center',alpha=1,color='b')
plt.title('GRAPPIC')
plt.xlabel('time')
plt.ylabel('kolichestbo')
plt.grid(True)
plt.show()
