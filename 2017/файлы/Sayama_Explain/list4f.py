
# -*- coding:utf-8 -*-
import sys

with open('result.txt', 'w') as fout:
	
	with open('5.txt', 'r') as f:
		line = f.readline()
		print(line, file=fout)
		print('----', file = fout)
		for line in f:
			print(line)
			a = list(map(str, line.split()))
			print(a, file=fout)


