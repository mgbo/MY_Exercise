
f=open('b4.txt','r')
b=[]
for line in f:
	a = line.split()
	print (a)
	t1=a[0]
	b.append(t1)
print (b)
print ('-------')

first=b[0]

for sec in b[1:]:
	if sec>first:
		print ("first = ", first)
		first=sec
		print ("second = ", first)
		print ("OK")
		
	else:
		print ("first =  ", first)
		first=sec
		print ("second = ", first)
		print ("WRONG")
		break

f.close()
