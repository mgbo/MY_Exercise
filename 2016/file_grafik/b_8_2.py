
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

print ("List : ", b)

lenb=len(b)
print ("len b :",lenb)

for i in range(0,lenb):
	#print "i is ",b[i]
	if i+1!=lenb:
		if b[i]!=b[i+1]:
			if i==b[i]:
				count=b.count(b[i])
				print (("i=%d number of b=%d count=%d")% (i,b[i],count))
				b[i]=b[i+1] 
				#print ("i=%d number of b=%d count=%d")% (i,b[i],count)
				c.append(count)
				print ("-----")

print ("c : ",c)
maxc=max(c)
print (maxc)

cc=c.index(maxc)

print (cc+1)

