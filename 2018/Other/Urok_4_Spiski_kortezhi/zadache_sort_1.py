
n = [3,6,-8,2,-78,1,23,-45,9]
#[-78, -45, 23, 9, -8, 6, 3, 2, 1]

def my(p):
	b = abs(p)
	return b
	
a = sorted(n,key=my,reverse=True)

print (a)
