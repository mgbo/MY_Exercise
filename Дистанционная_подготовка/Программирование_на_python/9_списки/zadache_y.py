
'''
Ферзи
'''

def read_pos():
	l_p = []
	for i in range(8):
		x, y = map(int, input().split())
		l_p.append((x, y))
	return l_p


def queen(x1, y1, x2, y2):
	if abs(x1+y1) == abs(x2+y2) or abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
		# print ("YES")
		return True
	else:
		# print ("NO")
		return False

def check_all():
	correct = True
	ll = read_pos()

	for i in range(len(ll)):
		x1, y1 = ll[i]
		for j in range(i+1, len(ll)):
			x2, y2 = ll[j]
			if not queen(x1, y1, x2, y2):
				correct = False
				break
	return correct


ans = check_all()

if ans:
	print ('YES')

else:
	print ('NO')

'''
l = [1,2,3,4,5]

for i in range(len(l)):
	for j in range(i+1, len(l)):
		print (i, j)

'''



