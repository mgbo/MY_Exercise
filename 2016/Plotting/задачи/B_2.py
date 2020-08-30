
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from sys import exit

time=[]
kolichestbo=[]

f=open('bet.log','r')
g=f.read().split('\n')
f.close()

t_start = 0
i = 0

for line in g:
	a=map(int,line.split())
	print "list :",a
	if not a:
		break

	if t_start == 0:
		t_start = a[0]
	print "t_start : ",t_start
		
	n = (a[0]-t_start)/60	# минут с начала теста
	print "минут с начала теста : ",n
	print ("i = %d n = %d")%(i, n)
	
	if n in time :
		kolichestbo[i-1] = kolichestbo[i-1] + 1
		
	else :
		time.append(n)
		kolichestbo.append(1)
		i+=1
		
	print "time : ",time
	print "количество : ",kolichestbo
	print '---------------'

print "Time :",time
print "количество :",kolichestbo

#numkolichestbo=len(kolichestbo)
#print "kolichestbo:k",numkolichestbo


plt.bar(time,kolichestbo,color='b')

plt.title('GRAPPIC')
plt.xlabel('time')
plt.ylabel('kolichestbo')

plt.grid(True)

plt.show()
