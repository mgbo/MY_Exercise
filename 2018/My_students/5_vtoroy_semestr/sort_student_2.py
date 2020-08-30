
n = int(input())

new = []
for i in range(n):
	name,mark = map(str, input().split())
	new.append((name,mark))

#print (new)

def sort_m(s):
	return (int(s[1])),s[0]

for k,v in sorted(new, key=sort_m):
	print (k,v)