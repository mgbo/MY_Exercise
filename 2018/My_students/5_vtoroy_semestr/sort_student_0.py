
n = int(input())

new = []

for i in range(n):
	name,mark = map(str,input().split())
	new.append((name,mark))

#print (new)

def first_name(s):
	n,m = s
	return n,m

def first_mark(s):
	n = s[0]
	m = -int(s[1])
	return m


ans = sorted(new,key=first_name)
for i in ans:
	print("{} {}".format(i[0],i[1]))

print ()

ans_1 = sorted(new,key=first_mark,)
for i in ans_1:
	print("{} {}".format(i[0],i[1]))



