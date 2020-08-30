

# -*- coding:utf-8 -*-
l = []
f = open('output_2.txt','w')
with open('write_test.txt','r') as f_1:
	for line in f_1:
		print (line)
		f.write(line)

f.close()
f_1.close()