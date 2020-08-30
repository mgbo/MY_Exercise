
# -*- coding: utf-8 -*-

f = open('num.txt','r')

new = []
for l in f:
	num = list(map(int,l.split()))
	new = new + num
	print (new)

print (new)
ans1 = min(new)
ans2 = max(new)
print (ans1,ans2)
f.close()
