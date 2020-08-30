

d = {}
m = []

with open('file_q.txt', 'r') as f:
	for i in f:
		i_s = i.split()
		mark = int(i_s[-1])

		m.append(mark)

		if mark in d:
			d[mark]+=1
		else:
			d[mark]=d.get(mark,1)

	m.sort()
	second = m[-2]
	#print (second)

print (second,d[second])

f.close()


