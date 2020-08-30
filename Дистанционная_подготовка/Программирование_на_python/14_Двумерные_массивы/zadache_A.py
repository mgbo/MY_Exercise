"""
row,col = map(int, input().split())

def input_M(row,col):
	s = [list(map(int, input().split())) for n in range(row)]
	return s

s = input_M(row,col)

max_n = 0
for i in range(row):
	for j in range(col):
		if s[i][j]>max_n:
			max_n = s[i][j]
			row,col = i, j

print (row,col)

"""

nm = input().split()  
n = int(nm[0])
m = int(nm[1])
max_i = 0
max_j = 0
a = [[int(j) for j in input().split()] for i in range(n)]

print (a)

for i in range(0, n): # n=3 ----- 0,1,2
    for j in range(0, m): # m=4 ----0,1,2,3
        if a[i][j] > a[max_i][max_j]:
            max_i = i
            max_j = j
print(max_i, max_j)




