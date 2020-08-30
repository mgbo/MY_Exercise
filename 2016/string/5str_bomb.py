import sys

for line in sys.stdin:
	#print line
	line=line[:-1]
	s=line.replace('bomb','watermelon')
	print (s)
