
n = [8,7,1,3,-1]
lenn = len(n) - 1
print (lenn)
def mysort(n):
	for i in range(0,lenn):
		for ii in range(0,lenn-i):
			print (n)
			if n[ii]>n[ii+1]:
				n[ii],n[ii+1]=n[ii+1],n[ii]
	return n

ans = mysort(n)
print (ans)

for x in range(0,4):
	for i in range(0,4-x):
		print (x,i)
