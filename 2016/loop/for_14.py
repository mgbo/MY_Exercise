
import sys

i = 0

#for line in sys.stdin:

line = input()

for c in line :
	if '(' == c:
		i+=1
	if ')' == c:
		i-=1
	if i < 0 :
		print ('NO')
		exit(0)


if i==0:
	print ('YES')

else:
	print ('NO')
exit(0)


