
line = input()

o = '([{<'
c = ')]}>'

d =[]

for x in line:
	#print ("x : ",x)

	if x in o:
		y = o.index(x)+1		
		d.append(y)

	elif x in c:
		y = -(c.index(x)+1)
	
		if  not d:
			print ("NO")
			break
		last = d.pop()

		#print ("main : ",d)
		#print ("y : {} ,last : {} ".format(y,last))
		
		if y + last !=0:
			print ("NO")
			break

else:
	if len(d)>0:
		print ("NO")
	else:
		print ("YES")





