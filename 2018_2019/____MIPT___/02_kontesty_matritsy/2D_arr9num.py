m = []

for irow in range(3):
	m.append(list(map(int, input().split())))

r = 0
for row in m:
	for num in row:
		if num == 7:
			print (r)
	r+=1
	

