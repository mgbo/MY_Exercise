

import math
n = int(input())

new = []
for i in range(n):
	x,y = map(int,input().split())
	new.append((x,y))

#print (new)

def qsort(s):
	x,y = s
	len_p = math.sqrt(((0-x)**2+(0-y)**2))
	#print ("len_p : ",len_p)
	return len_p,x,y
'''
ans = sorted(new,key=qsort)
#print ("------------")
for i in ans:
	print (i[0],i[1])
'''

ans_1 = sorted(new,key=lambda s: math.sqrt((0-s[0])**2+(0-s[1])**2))

for i in ans_1:
	print (i[0],i[1])



