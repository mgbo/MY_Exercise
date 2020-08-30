
# -*- coding:utf-8 -*-

input = open('input.txt','r')
output = open('output.txt','w')

'''
#--------- только один слова ---------
c = input.read(1)
output.write(c)
'''
c = input.read(1)

while len(c)>0:
	output.write(c)
	c = input.read(1)

input.close()
output.close()
