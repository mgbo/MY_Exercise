

some_list = [-5, -1, -13, -11, 4, 8, 16, 32]

max_list = max(n for n in some_list if n<0)
print (max_list)

min_list = min(n for n in some_list if n>0)
print (min_list)



t = ['-1','11','-11','12']

for i in t:
	print (i)

t2 = list([map(int,num) for num in t])
print (t2)