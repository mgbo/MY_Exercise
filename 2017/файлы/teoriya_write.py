
# -*- coding:utf-8 -*-

f = open('output_1.txt','w')
N = int(input())
for i in range(N):
	sar = input()
	f.write(sar + '\n')

f.close()
