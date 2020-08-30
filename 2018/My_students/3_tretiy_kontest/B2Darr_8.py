

def read_matx():
	matx = []
	for i in range(3):
		row = list(map(int,input().split()))
		matx.append(row)
	return matx

def print_matx(m):
	for i in range(len(m)):
		print (*m[i])

def dirg(m):
	summa = 0
	for i in range(len(m)):
		summa += m[i][2-i]
	return summa


m = read_matx()
#print_matx(m)
ans = dirg(m)
print(ans)