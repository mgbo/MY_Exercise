
#Много строк через readline
#sys.readline() - прочитать 1 строку

import sys

fp = sys.stdin
s = fp.readline()

print ('Первая строка : ', s)

while  s:
	#print (s)
	s = fp.readline()
	print (s)


