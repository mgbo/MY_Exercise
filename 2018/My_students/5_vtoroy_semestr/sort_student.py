
n = int(input())

new = []

for i in range(n):
	name,mark = map(str,input().split())
	new.append((name,mark))

#print (new)

def first_mark(s):
	n = s[0]
	m = -int(s[1])
	return m,n

ans_1 = sorted(new,key=first_mark)
for i in ans_1:
	print("{} {}".format(i[0],i[1]))



