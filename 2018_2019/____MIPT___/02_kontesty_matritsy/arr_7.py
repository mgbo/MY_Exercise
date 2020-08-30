
def read_matrix(r,c):
	a = []
	for i in range(r):
		a.append(list(map(int, input().split())))
	return a

def sum_matrix(l, l1):
	res = [[i*0 for i in range(c)] for j in range(r)]
	# print ('role: {}, colum: {}'.format(r,c))
	for i in range(len(l)):
		for j in range(len(l[0])):
			res[i][j] = l[i][j] + l1[i][j]
	return res

def print_matrix(l):
	for i in l:
		for j in i:
			print (j, end=' ')
		print()

r,c = map(int, input().split())

l1 = read_matrix(r,c)
l2 = read_matrix(r,c)
ans = sum_matrix(l1, l2)
print_matrix(ans)





