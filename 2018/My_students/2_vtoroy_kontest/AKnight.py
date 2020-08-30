
def Pchange(a):
	if(a == 0):
		a = 1
	else:
		a = 0
	return a

def Pnext(a, b):
	if(a == 0):
		b = Pchange(b)
	return b

def Pprog(s, f):
	isknight = f
	res = 0
	if isknight == 1:
		res += 1
		
	for p in s[:-1:]:
#		print('isknignt=%d p=%d res=%d' % (isknight, p, res))
		p = Pnext(isknight, p)
		if p == 1:
			res += 1
		isknight = p
#	print(res)
	return res

int(input())
a = list(map(int, input().split()))
#print(a)

#print('-----')
m = Pprog(a, 1)
#print('-----')
n = Pprog(a, 0)
print(min(m,n))

#~ if(Pnext(m[x-1], s[0]) == 1):
	#~ print(m.count(1))
#~ else:
	#~ print(n.count(1))
