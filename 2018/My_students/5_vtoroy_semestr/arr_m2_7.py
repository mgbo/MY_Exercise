
n = list(map(int, input().split()))

#print (n[-1::-1])
for i,x in enumerate(n):
	if x>0:
		l = i
		break
for i,x in enumerate(n):
	if x<=0:
		r=i

n[l], n[r] = n[r], n[l]
print (*n)