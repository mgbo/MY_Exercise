

def idn(n):
	last = -1
	for i in range (len(n)):
		if n[i]>=0:
			last = i
			#print (i,n[i])
	return last


n = list(map(int,input().split()))

print (idn(n))
