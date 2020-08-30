
n = int(input("Enter a number : "))


for i in range(1,n+1):
	for j in range(n):
		for k in range(n):
			# print (i, j, k)
			if i+j+k == 3:
				print (i,j,k)
	# print ()