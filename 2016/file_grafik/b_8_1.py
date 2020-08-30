# -*- coding: utf-8 -*-
b=[]

f=open('bet8_1.log','r')

for line in f:
	a=line.split()
	print (a)
	if not a:
		break
	t3=a[1]
	b.append(t3)

print (b)

print ('--------')

b.sort();

print ("sort : ",b)

first=b[0]

c=[]
d=[]

lenb=len(b)
print ("len b :",lenb)


#for line in b[0:]:
#print "first :",first
#print "line : ",line
for i in range(0,lenb):
  #print "i is ",b[i]
  if i+1!=lenb:
   if b[i]!=b[i+1]:
    count=b.count(b[i])
    print ("i=%d number of b=%d count=%d")% (i,b[i],count)
    #b[i]=b[i+1] 
    #print ("i=%d number of b=%d count=%d")% (i,b[i],count)
    c.append(count)
    d.append(b[i])
    print ("-----")
   if b[i]==b[-1]:
    count=b.count(b[i])
    print ("i=%d number of b=%d count=%d")% (i,b[i],count)
    c.append(count)
    d.append(b[i])
    break
    
print ("запись : ",d)
print ("колечество записей : ",c)

maxc=min(c)
#print maxc
cc=c.index(maxc)
#print cc

ans=d[cc]
print ("Минимальное количество записей об одном клиенте = %d ")% (ans)

