
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# print (A+B)

def Merge(A,B):
	new = A + B
	return new

ans = Merge(A, B)
print (*(sorted(ans)))