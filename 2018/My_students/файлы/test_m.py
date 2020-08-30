
def Matrix_1(n):
	matx = []
	for i in range(n):
		line = input()
		matx.append(list(map(int,line.split())))
	return matx

def display(m):
	for row in m:
		print (*row)

def transposed(m):
	tran = []
	for i in range(4):
		tran_row = []
		for row in m:
			tran_row.append(row[i])
		tran.append(tran_row)
	return tran

n = int(input())
ans_m = Matrix_1(n)
display(ans_m)

print ('-'*10)
tan_ans = transposed(ans_m)
display(tan_ans)


