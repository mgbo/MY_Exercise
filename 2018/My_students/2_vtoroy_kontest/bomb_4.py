
import sys

find = 0

for word in sys.stdin :
	#print (word)
	find += word.find("bomb")
	#if ans!=-1:
	#	find+=1

print (find)
