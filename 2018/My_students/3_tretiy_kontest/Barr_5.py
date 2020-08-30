
a = list(map(int,input().split()))

k,n = map(int,input().split())

for i in a[k:n+1:]:
	print (i,end=' ')
	
