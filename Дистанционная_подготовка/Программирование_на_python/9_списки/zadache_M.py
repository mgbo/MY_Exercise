
n = list(map(int, input().split()))
leng_n = len(n)

for i in range(len(n)//2):
	n[i], n[leng_n-(i+1)] = n[leng_n - (i+1)], n[i]
	# print (*n)

print (*n)