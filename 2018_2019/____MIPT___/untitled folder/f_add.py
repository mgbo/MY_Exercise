
d,n,k = map(int,input().split())


i=0
total = 0

while i<d:
	total +=n
	print ("day {} --->number of pages :{}".format(i+1,n))
	n//=i+2
	i+=1

print (total+k)