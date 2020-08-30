

b = list(map(int, input().split()))
#print (b)

bb = set()
#print (bb)

for x in b:
	if not x in bb:
		print (x, end=' ')
		bb.add(x)

# v-2
"""
a = []
for x in b:
	if not x in bb:
		bb.add(x)
		print (bb)
		a.append(x)
		print (a)

print (*a)
"""

