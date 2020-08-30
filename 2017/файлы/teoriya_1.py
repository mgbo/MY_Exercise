
# -*- coding:utf-8 -*-

'''
import sys

for line in sys.stdin:
	print line
	pair = line.split()
	print pair
'''

f = open('file.txt','r') #открыть файл file.txt на чтение

str_1 = f.read() # прочитать весь файл в переменную str_1

print str_1

f.close()