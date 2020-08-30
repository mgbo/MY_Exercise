
n = int(input())

if n%3==0 or n%5==0:
	if n%15!=0:
		print ("YES")
	else:
		print ("NO")
else:
	print ("NO")
