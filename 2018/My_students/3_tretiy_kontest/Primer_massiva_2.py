

def read_v1():
	m = []
	for i in range(4):
		m.append(list(map(int,input().split())))
	return m

def auto_zero(m):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if i<j:
				m[i][j] = 0
			elif i>j:
				m[i][j] = 2
			else:
				m[i][j] = 1

def pri_matri(m):
	for row in m:
		print (' '.join(list(map(str,row))))
	print ()

m = read_v1()
pri_matri(m)
auto_zero(m)
pri_matri(m) 
'''
1 0 0 0
2 1 0 0
2 2 1 0
2 2 2 1
'''





