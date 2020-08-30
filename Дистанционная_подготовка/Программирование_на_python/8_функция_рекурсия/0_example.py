
def max(a,b):
	if a>b:
		return a
	else:
		return b

def max3(a,b,c):
	return max(max(a,b),c)

a,b,c = map(int, input().split())
print (max3(a,b,c))

