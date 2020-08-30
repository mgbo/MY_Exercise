
n = int(input())

l = list(map(int, input().split()))

ll = set(l)

unique = []
for i in ll:
	if l.count(i)==1:
		unique.append(i)

if unique:
	print(*unique)
else:
	print (-1)


'''
output = []

for i in l:
	if i not in output:
		output.append(i)

print (output)




res = set()
for i in l:
	res.add(i)

print (res)
'''



