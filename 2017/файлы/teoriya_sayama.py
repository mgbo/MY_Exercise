
# -*- coding:utf-8 -*-

fout = open('file.txt','a')
# file_1.txt довабляется в file.txt. 
# для этого нужно использовать 'a'

with open ('file_1.txt','r') as f:
	#line = f.readline()
	#print (line,file=fout)
	#print ("---------------")
	for line in f:
		print (line)
		a = list(map(int,line.split()))
		print (a,file=fout)
