
# k, l, m, n = (int(input()) for _ in range(4))

# print (k, l, m, n)

k,l,m,n = map(int, input().split())

def queen_chess(k, l, m, n):
	if abs(k-m) == abs(l-n) or k == m or l == n:
		print ("YES")
	else:
		print ("NO")


queen_chess(k, l, m, n)