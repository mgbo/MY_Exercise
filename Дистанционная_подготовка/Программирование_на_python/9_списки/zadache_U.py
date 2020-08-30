
n = list(map(int, input().split()))

new = []

for i in n:
	if n.count(i)>=1:
		if i not in new:
			new.append(i)

#print (new)
print (len(new))