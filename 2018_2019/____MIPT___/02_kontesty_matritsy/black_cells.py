
n = int(input())

def read_kletok(n):
	kletok = []
	for i in range(n):
		kletok.append(list(map(str,input().split())))
	return kletok

def output_kletok(l):
	for irow in l:
		for i in irow:
			print (i, end=' ')
		print()

def check_kolichestvo(l):
	count = 0
	for irow in l:
		for i in irow:
			count += i.count('*')
	return count

kle = read_kletok(n)
# output_kletok(kle)
ans = check_kolichestvo(kle)
print (ans)


