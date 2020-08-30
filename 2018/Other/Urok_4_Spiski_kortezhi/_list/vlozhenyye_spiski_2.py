
vec = [-4,-2,0,2,4]
print (vec)

vec_sqr = [x*2 for x in vec]
print (vec_sqr)

# if x>=0
vec_if = [x for x in vec if x>=0]
print (vec_if)

vec_abs = [abs(x) for x in vec]
print (vec_abs)

# call a method on each element
freshfruit = [' banana',' loganberry',' passion fruit']
print (freshfruit)
ele = [weapon.strip() for weapon in freshfruit]
print (ele)

double_num = [(x,x**2) for x in range(5,10)]
print (double_num)

#------------ Matrix --------------------
matrix = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
]

print (matrix)

# ее транспонировать

transposed = []
for i in range(len(matrix)+1):
	transposed.append([row[i] for row in matrix])

print (transposed)

'''
for i in range(4):
	for row in matrix:
		print (row[i])
'''

for row in matrix:
		print (row[0])







