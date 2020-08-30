
'''
a = []
n = map(int,input().split())

for i in n:
	a.append(i)

print (a)

a.sort()

print (a)

b = a[2:]
print (b)

res = sum(b)/len(b)

print (res)

'''

m = [[10,8,7,3,4,2,1],[2,4,6,8,7,10]]

minm=[]
remin=[]

'''
for minm in m:
	minm.sort(reverse=True)
	remin=minm[:-2]
	print (sum(remin)/len(remin))
'''

def my(p):
	for minm in p:
		minm.sort(reverse=True)
		print (minm)
		remin=minm[:-2]
		print (sum(remin)/len(remin))

my(m)
