
f=open('bet_3_2.log','r')
b=[]

for line in f:
	a = line.split()
	print (a)
	if not a:
		break
	t2=a[2]
	b.append(t2)
	
count=0
b.sort()

check_1 = b[0]
print (check_1)

for check_2 in b[1:] :
	if check_2 == check_1:
		print ('check = {} and check_2 {} '.format(check_1,check_2))
		count +=1 
	check_1= check_2

print ("Worng of check : ",count)
f.close()




