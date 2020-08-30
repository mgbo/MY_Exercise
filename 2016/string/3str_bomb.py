
import sys

for line in sys.stdin:
	s=line.lower()
	#print s
	if 'bomb' in s:
		print 'YES'
		exit(0)
else:
	print 'NO'
		

