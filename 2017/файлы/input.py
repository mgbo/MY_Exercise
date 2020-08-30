
# -*- coding:utf-8 -*-
import sys

with open ('file_1.txt','r') as f:
	line = f.readline()
	print (line)
	print ("---------------")
	for line in f:
		print (line)
		a = list(map(int,line.split()))
		print (a)
