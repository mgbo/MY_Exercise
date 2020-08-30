
A = [[1,2,3],[4,5,6],[7,8,9]]

def print_M(A):
	s=''
	for row in range(len(A)):
		for col in range(len(A[row])):
			s+=str(A[row][col])+' '
		s=s+'\n'
	return s.strip()

def print_M_1(A):
	for i in range(len(A)):
		for j in range(len(A[i])):
			print (A[i][j],end=' ')
		print()

def display(A):
	for row in A:
		for elem in row:
			print (elem,end=' ')
		print ()


#print(print_M(A))
print_M_1(A)
print ("----------")

for row in A:
	print(' '.join(list(map(str, row))))








