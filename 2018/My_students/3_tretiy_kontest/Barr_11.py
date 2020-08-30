

a = list(map(int,input().split()))
summa = 0
for i in range(len(a)):
	if i>2:
		summa += a[i]

print (summa)