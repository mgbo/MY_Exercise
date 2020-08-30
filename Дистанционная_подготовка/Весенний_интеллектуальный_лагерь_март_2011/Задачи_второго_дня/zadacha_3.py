

k,l,m,n = map(int, input().split())

def bishop_chess(k,l,m,n):

	if abs(k-m) == abs(l-m):
		print ("Да")
	else:
		print ("Нет")

bishop_chess(k,l,m,n)