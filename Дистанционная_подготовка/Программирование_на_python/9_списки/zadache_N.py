
l = list(map(int, input().split()))

i = 0
for _ in range(len(l)//2):
	l[i], l[i+1] = l[i+1], l[i]
	i +=2

print (*l)