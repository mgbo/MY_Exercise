'''
правило ход конь (щхматы)
'''

k,l,m,n = map(int, input().split())

def queen_chess(k, l, m, n):
	f = abs(k - m)
	s = abs(l - n)

	if abs (f - s) == 1:
		print ("YES")
	else:
		print ("NO")


queen_chess(k, l, m, n)

'''
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (abs(x1 - x2) == 2 and abs(y1 - y2) == 1) or (abs(x1 - x2) == 1 and abs(y1 - y2) == 2):
    print ("YES")
else:
    print ("NO")
'''




