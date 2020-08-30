
with open('file_G.txt', 'r') as f:
	for line in f:
		#print (line)
		if '@' in line:
			print ("YES")
			break
	else:
		print ("NO")