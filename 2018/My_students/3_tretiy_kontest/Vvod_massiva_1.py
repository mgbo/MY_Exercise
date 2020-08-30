
# -------- vrain 1 ---------

def read_v1():
	m = []
	for i in range(3):
		m.append(list(map(input().split())))
	return m

# ----------- vrain 2 -----------

def read_v2():
	m = []
	for i in range(3):
		row = input().split()
		for i in range(len(row)):
			row[i] = int(row[i])
		m.append(row)
	return m

# ------- vrain 3 --------------

def read_3():
	m = [list(map(int, input().split()) for i in range(3))]
	return m

def pri_matri(m):
	for row in m:
		print (' '.join(list(map(str,row))))
	print ()

m = read_v2()
pri_matri(m)

















