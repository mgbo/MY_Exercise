import sys

for line in sys.stdin:
	print(line)
	a = list(map(str, line.split()))
	print(a)


