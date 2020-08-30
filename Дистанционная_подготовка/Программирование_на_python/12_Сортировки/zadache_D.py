
l = list(map(int, input().split()))
# print (l)


def OppositeNumbers(l):
	new = []

	for i,n in enumerate(l):
		ans = l.count(-(n))
		if ans != 0:
			# print (i, n)
			new.append(i)

	return new


ans = OppositeNumbers(l)
print (*ans)