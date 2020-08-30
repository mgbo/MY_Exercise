
n = list(map(int,input().split()))

def idn(n):
	for i in range (len(n)):
		if n[i]>0:
			#print (i,n[i])
			return i
	return -1

print (idn(n))
