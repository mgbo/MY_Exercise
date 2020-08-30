
n = list(map(int, input().split()))
length = len(n) - 1

for i in range(length):
	for j in range(length):
		n[j], n[j+1] = n[j+1], n[j]

print (*n)