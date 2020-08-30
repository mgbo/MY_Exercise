
import sys

find = 0

for word in sys.stdin.read().split() :
	print (word)
	if word=="bomb":
		find+=1

print (find)
