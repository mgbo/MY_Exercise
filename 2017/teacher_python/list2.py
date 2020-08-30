import sys

for line in sys.stdin:
	print(line)
	a = list(map(int, line.split()))
	print(a)


