

n = list(map(int, input().split()))

i = 0

while i < len(n) - 1:
	m = i
	j = i + 1

	while j < len(n):
		if n[j] < n[m]:
			m = j
		j +=1

	n[i], n[m] = n[m], n[i]

	i +=1

print (n)
