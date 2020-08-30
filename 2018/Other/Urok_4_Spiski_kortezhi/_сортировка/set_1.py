
n = [1,3,5,6,7,8,9,1,4,5,6,7]

print (n)
nn = set(n)
print (nn)

for i in nn:
	con = n.count(i)
	print (i,con)
