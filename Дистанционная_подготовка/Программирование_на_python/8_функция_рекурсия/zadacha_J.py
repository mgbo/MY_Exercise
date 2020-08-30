
n = int(input())

def IsPrime(x):
	d = 2
	while x % d !=0 :
		print (d)
		d += 1

	return d


IsPrime(n)

if IsPrime:
	print ("YES")

else:
	print ("NO")