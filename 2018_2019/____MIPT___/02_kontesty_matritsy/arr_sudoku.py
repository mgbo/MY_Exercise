
sudoku = []

for i in range(9):
	sudoku.append(list(map(int,input().split())))

def print_normal(l):
	for irow in l:
		for n in irow:
			print(n, end=' ')
		print()
	print('-----------\n')


def print_3(l, rs, re, cs, ce):
	for irow in l[rs:re]:
		for n in irow[cs:ce]:
			print (n, end=' ')
		print()

# print_3(sudoku, 0,3, 6, 9)

def merge_3(l, rs, re, cs, ce):
	new_sudoku = []
	for irow in l[rs:re]:
		for n in irow[cs:ce]:
			new_sudoku.append(n)
	return new_sudoku


def print_all(l):
	a = 0
	b = 3
	c = 0
	d = 3
	for j in range(3):
		for jj in range(3):
			print_3(l, a, b, c, d)
			print ('------')
			# print ("({},{})---->({},{})".format(a,b,c,d))
			c +=3
			d +=3
		a +=3
		b +=3
		c = 0
		d = 3
		print('++++++++++++++')

# print_all(sudoku)



def check_3(l):
	a = 0
	b = 3
	c = 0
	d = 3
	i = 0
	for j in range(3):
		for jj in range(3):
			# print_3(l, a, b, c, d)
			# print ('------')
			f_3 = merge_3(l, a, b, c, d)

			if len(set(f_3)) == 9:
				# print ('OK')
				i +=1
			# else:
			# 	print('False')
			# print ('------')
			# print ("({},{})---->({},{})".format(a,b,c,d))
			c +=3
			d +=3
		a +=3
		b +=3
		c = 0
		d = 3
	return i

def check_role(l):
	i = 0
	for i in range(9):
		#print(l[i])
		if len(set(l[i])) == 9:
			i+=1
		#print ('-----------')
	# print ('i:',i)
	return i

# check_role(sudoku)

def change_col(l):
	new_all = []
	for i in range(9):
		new = []
		for j in range(9):
			new.extend([l[j][i]])
		new_all.append(new)
	return new_all


new_sudoku = change_col(sudoku)
# print_normal(new_sudoku)
# print (check_role(new_sudoku))

if check_3(sudoku) == 9 and check_role(sudoku) == 9 and check_role(new_sudoku) == 9:
	print ("YES")
else:
	print ("NO")




















