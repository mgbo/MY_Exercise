
'''

Пересечение множеств

'''

A = list(map(int, input().split()))
B = list(map(int, input().split()))



def Intersection(A, B):
	new = []
	for i in range(len(set(A))):
		for j in range(len(set(B))):
			if A[i] == B[j]:
				new.append(A[i])

	return new

ans = Intersection(A, B)
print (*ans)


'''
def Intersection_1(A, B):
	a = set(A)
	b = set(B)

	inter = a&b
	return inter
'''


