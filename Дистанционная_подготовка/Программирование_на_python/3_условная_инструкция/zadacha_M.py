
'''
правило ход конь (щхматы)
'''

# k,l,m,n = map(int, input().split())

k = int(input())
l = int(input())
m = int(input())
n = int(input())

def queen_chess(k, l, m, n):
	f = abs(k - m)
	s = abs(l - n)

	if abs (f - s) == 1:
		print ("YES")
	else:
		print ("NO")


queen_chess(k, l, m, n)
