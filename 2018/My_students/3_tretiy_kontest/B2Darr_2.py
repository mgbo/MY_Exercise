
def read_matx():
	matx = []
	for i in range(3):
		row = list(map(int,input().split()))
		matx.append(row)
	return matx

def print_matx(m):
	for row in m:
		print (*row)

m = read_matx()
m[1][2] =m[1][2]*10
print_matx(m)