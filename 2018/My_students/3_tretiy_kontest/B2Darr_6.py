

def read_matx():
	matx = []
	for i in range(3):
		row = list(map(int,input().split()))
		matx.append(row)
	return matx

def print_matx(m):
	for i in range(len(m)):
		print (*m[i])


m = read_matx()
cen = m[1]
#print (cen)
print (sum(cen))