import sys

fout = open('result.txt', 'w')

with open('5.txt', 'r') as f:
	line = f.readline()
	print(line, file=fout)
	print('----')
	for line in f:
		print(line)
		a = list(map(int, line.split()))
		print(a, file=fout)

fout.close()

