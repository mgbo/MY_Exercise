
inf = list(map(str,input().split('.')))

# print (len(inf))

if len(inf) == 4:
	for i in inf:
		if int(i) >255 and int(i)>0:
			print ("NO")
			break
	else:
		# print (i)
		print ('YES')

else:
	print ("NO")




