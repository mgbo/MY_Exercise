
def SwapC(a):
	l = len(a)
	for i in range(l):
		a[i],a[-1] = a[-1] , a[i]
		#print (a)
	#print ("------")

nn = int(input())
n = list(map(int,input().split()))

SwapC(n)
print (*n)
