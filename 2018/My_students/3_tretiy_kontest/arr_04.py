
def SwapC(a,d):
	l = len(a)
	for i in range(d):
		for i in range(l):
			a[i],a[-1] = a[-1] , a[i]
			#print (a)
	#print ("------")

nn = int(input())
n = list(map(int,input().split()))
d = int(input())

#print (n)
#print ("-------")
SwapC(n,d)
print (*n)
