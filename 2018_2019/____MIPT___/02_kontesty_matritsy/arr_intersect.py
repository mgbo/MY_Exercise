
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a>b:
	first = a
	sec = b
else:
	first = b
	sec= a

# print ('long :',first, type(first))
# print ('short :',sec)

first.sort()
sec.sort()

ans = []
for i in range(len(sec)):
	if sec[i] in first:
		first.remove(sec[i])
		ans.append(sec[i])

print (*ans)

