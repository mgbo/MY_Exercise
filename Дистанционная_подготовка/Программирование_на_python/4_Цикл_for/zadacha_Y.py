
n = int(input())

cur = 1
k = 0

for i in range(n):
	print (cur, end=' ')
	k = k + 1
	# print ()
	# print (cur,k)
	if k == cur:
		k = 0
		cur = cur + 1

print ()
