

a = int(input())
b = int(input())
c = int(input())
d = int(input())

def min4(a, b, c, d):
	min_number = min(min(a,b), min(c,d))
	return min_number

ans = min4(a, b, c, d)
print (ans)