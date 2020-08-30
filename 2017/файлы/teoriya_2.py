
# -*- coding: utf-8 -*-

f = open('file.txt','r')

'''
line = f.readline() # отдельно читаем первую строку

print line

while line:
	print line
	line = f.readline() # читаем все остальные строки

f.close()
'''

for line in f:
	print line
f.close()
