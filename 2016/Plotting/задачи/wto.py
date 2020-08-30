
# -*- coding: utf-8 -*-

import sys
time=[]
kolichestbo=[]

t_start = 0
i = 0
interval=60

for line in sys.stdin:
	a=map(int,line.split())
	print (a)
	
	if t_start==0:
		t_start=a[0]
	print ("start : ",t_start)
	
	print ("a[0]=%d t_start=%d")% (a[0],t_start)
	n=(a[0]-t_start)/interval
	print ("i=%d n=%d")% (i,n)
	print ("время : ",time)
	
	if n*interval in time:
		print ("if : ",(n,time))
		kolichestbo[i-1]=kolichestbo[i-1]+1
		print ("kolichestbo[i-1] = ",kolichestbo[i-1])
		
	else :
	 print ("else : ", (n,time))
	 time.append(n*interval)
	 kolichestbo.append(1)
	 i+=1
	 print ("i= : ",i)
		
	print ("Time : ",time)
	print ("количество : ",kolichestbo)
	print ('---------------')

	

	

