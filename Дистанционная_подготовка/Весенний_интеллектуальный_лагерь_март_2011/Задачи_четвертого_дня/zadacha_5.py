
n = int(input())

for i in range(1,n+1):
	for j in range(i,n+1):
		for k in range(j,n+1):
			ans = i+j+k
			if  ans == n:
				print ("{}+{}+{}={}".format(i, j, k, ans))

