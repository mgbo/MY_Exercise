
def read_matx():
	matx = []
	for i in range(3):
		row = list(map(int,input().split()))
		matx.append(row)
	return matx

def print_matx(m):
	for i in range(len(m)):
		print (*m[i])

def dirg_right(m):
	summa = 0
	for i in range(len(m)):
		summa += m[i][2-i]
	return summa

def dirg_left(m):
	summa = 0
	for i in range(len(m)):
		summa += m[i][i]
	return summa

def row_0(m):
	ans = m[0]
	#print (ans)
	return (sum(ans))

def row_1(m):
	ans = m[1]
	return (sum(ans))

def row_2(m):
	ans = m[2]
	return (sum(ans))

def col_0(m):
	summa = 0
	for i in range(len(m)):
		summa +=m[i][0]
	return summa

def col_1(m):
	summa = 0
	for i in range(len(m)):
		summa +=m[i][1]
	return summa

def col_2(m):
	summa = 0
	for i in range(len(m)):
		summa +=m[i][2]
	return summa

def Mag(m):
	if dirg_left(m) == dirg_right(m) == row_0(m) == row_1(m) == row_2(m) == col_0(m) == col_1(m) == col_2(m):
		print ("MAGIC")


m = read_matx()
Mag(m)



