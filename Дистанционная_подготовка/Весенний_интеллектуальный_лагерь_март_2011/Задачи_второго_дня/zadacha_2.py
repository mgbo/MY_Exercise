
k,l,m,n = map(int, input().split())

def rook_chess(k,l,m,n):
	if k == m or l == n:
		print ("Да")
	else:
		print ("Нет")

rook_chess(k,l,m,n)