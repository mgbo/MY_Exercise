
#A = [[1,2,3],[4,5,6],[7,8,9]]

def print_M(A):
	s=''
	for row in range(len(A)):
		for col in range(len(A[row])):
			s+=str(A[row][col])+' '
		s=s+'\n'
	return s.strip()

def input_M(n):
	A = []
	for i in range(n):
		A.append(list(map(int, input().split())))
	return A


n = int(input())
B = input_M(n)
ans = print_M(B)
print (ans)




