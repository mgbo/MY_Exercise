
l = list(map(int, input().split()))
n = int(input())

def Big_shift(l):
	length = len(l) - 1
	for i in range(length):
		for j in range(length):
			l[j], l[j+1] = l[j+1], l[j]

	return l

for _ in range(n):
	ans = Big_shift(l)

print (*ans)

