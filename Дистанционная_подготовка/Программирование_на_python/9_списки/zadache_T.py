
n = list(map(int, input().split()))

new = []
for i in n:
	if n.count(i)==1:
		new.append(i)

print(*new)