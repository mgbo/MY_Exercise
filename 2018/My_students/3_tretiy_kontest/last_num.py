
def Last(a):
	ilast = -1
	for i in range(len(a)):
		if a[i] == 7:
			ilast = i
			print (i,a[i])
	return ilast


a = [9,-3,7,7,2,1,7,8,9]

print (Last(a))
