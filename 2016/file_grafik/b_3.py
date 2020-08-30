
b=[]
f=open('bet_3_2.log','r')

for line in f:
	a=line.split()
	print (a)

	t3=a[2]
	b.append(t3)

print (b)
print ('--------')

first=b[0]

for sec in b[1:]:
	if first<sec:
		print ("first = ", first)
		first=sec
		print ("second = ",first)
		print ("OK")
	else:
		print ("first = ", first)
		first=sec
		print ("second = ", first)
		print ("WRONG")
		break

else:
	print ("OK!!")
f.close()
