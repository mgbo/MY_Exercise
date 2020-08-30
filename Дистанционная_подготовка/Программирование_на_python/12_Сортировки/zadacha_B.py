

n = list(map(int, input().split()))

ind = 0
max_n = n[0]

for i in n[1:]:
	if max_n <= i:
		max_n = i
		indd = ind

	ind +=1

print (max_n,indd)
