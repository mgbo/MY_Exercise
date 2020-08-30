import sys

with open('5.txt', 'r') as f:
	for line in sorted(f):
		print(line)
		a = list(map(str, line.split()))
		print(a)


