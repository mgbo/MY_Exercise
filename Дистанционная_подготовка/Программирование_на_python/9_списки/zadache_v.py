
s = list(map(int, input().split()))
max = s[0]
print (max)

max_count = s.count(max)
#print (max_count)

for el in s:
	if s.count(el)>max_count:
		max = el
		max_count = s.count(el)

print(max)
