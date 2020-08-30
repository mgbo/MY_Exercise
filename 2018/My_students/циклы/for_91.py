

r = int(input())
c = int(input())

for row in range(r):
	for col in range(c):
		if row==0 or row==r-1 or col==0 or col==c-1:
			print ("*",end='')
		else:
			print (" ", end='')
			
		if col==c-1:
			print('') # new line
		#elif (row!=0 and col==0):
		#	print ("*",end=' '*(c-2))
		#elif (row!=r-1 and col==c-1):
		#	print ("*",end='')
	print ()

