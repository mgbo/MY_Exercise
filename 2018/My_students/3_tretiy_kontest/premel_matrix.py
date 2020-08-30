

'''
row = [1,2,3,4]

for i in range(len(row)):
	print (row[i], end=' ')

print ()

row_1 = [i for i in range(1,5)]
print (row_1)
'''
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]


print (matrix)
print (matrix[0][1]) #2


# способ 1
for i in range(len(matrix)):
	for ii in range(len(matrix[i])):
		print (matrix[i][ii], end = ' ')
	print ()

print ("----------")

# способ 2
for row in matrix:
	for x in row:
		print (x, end= ' ')
	print()

# for print matrix
def printtab(m):
	for row in m:
		print (*row)

print ("----------")
printtab(matrix)


'''
t = []
t = [[row[i] for row in matrix] for i in range(len(matrix))]
print (t)

'''

n = int(input())
m = []
for irow in range(n):
	row = list(map(int, input().split()))
	m.append(row)

printtab(m)

def testtab():
	m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
	return m





