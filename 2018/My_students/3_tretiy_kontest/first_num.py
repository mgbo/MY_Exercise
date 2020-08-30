
def first(a):
	i7 = -1
	for i in range(len(a)):
		if a[i] == 7:
			print (i,a[i])
			return i
		print ("на нашли 7 !")


a = [9,-3,7,7,2,1,7,8,9]

print (first(a))
