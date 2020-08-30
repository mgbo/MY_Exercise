
'''
col = ['blue', 'green', 'red', 'red', 'yellow', 'blue']

d = {}
for i in range(len(col)):
	if col[i] not in d:
		d[i] = col[i]

d = sorted(d.items(), reverse=True)

print (d)
'''
d = []
for i in range(3):
	x, y, z = input().split()
	d.append([x,y,z])

print (d)
