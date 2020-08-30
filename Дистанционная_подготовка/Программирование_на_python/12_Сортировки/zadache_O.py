
n = int(input())
ss = list(map(int, input().split()))

d = {}
for i in ss:
	d[i]=d.get(i,0)+1

def sort_v(s):
	return s[1]

print (d)