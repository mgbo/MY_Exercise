
n=int(input())

def fac(n):
	if n==0:
		return 1
	else:
		#print (n)
		res = n * fac(n-1)
		print ("intermediate result for ",n , " * fac(" , n-1, "): ", res)
		return res
		
		


print (fac(n))
