
n = int(input())
m = []
for i in range(n):
	line = input()
	print('--%s--' % line)
	m.append(list(map(int, line.split())))

print (m)
print ('-------------------')
mT = zip(*m)
print(*mT)

print ("================")
mT = [list(r) for r in zip(*m)]
print(*mT)

