
m = map(int, input().split())

max1 = 0
max2 = 0

for n in m:
	if max1 < n:
		max1 = n
		print ("Max1 : ", max1)

print (max1)