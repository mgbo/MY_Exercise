

l = list(map(int, input().split()))
n = int(input())

for _ in range(n):
	p = l.pop()
	l.insert(0, p)

print (*l)