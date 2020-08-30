
# -*- coding: utf-8 -*-

nob=[1,1,6,2,5,3,2,1,2,5,1]

print (nob)

sl=set(nob)
print ('----')
print (sl)

a={}
b=[]
for n in set(nob):
	#print "n : ",n
	p=nob.count(n)
	a[n]=p
	print (n,p)
	#b.append(p)

#print b


#ans=[cc]
#print ("Минимальное количество записей об одном клиенте = %d ")% (ans)
