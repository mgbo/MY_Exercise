
def first(a):
	for i in range(len(a)):
		if a[i] >0:
			#print (i,a[i])
			return i

def Last(a):
	ilast = -1
	for i in range(len(a)):
		if a[i]<=0:
			ilast = i
			#print (i,a[i])
	return ilast


def swap(a):
	fin = first(a)
	lin = Last(a)
	a[fin],a[lin] = a[lin],a[fin]

n = list(map(int,input().split()))

swap(n)

print (*n)
