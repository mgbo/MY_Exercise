
a = map(int,input().split())

total = 0
for x in a:
	if x<0:
		total = total + x 

print (total)