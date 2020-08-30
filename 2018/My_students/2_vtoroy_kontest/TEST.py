
'''
import sys

for word in sys.stdin:
	#print (word)
	#print (type(word))
	re = word.replace("bomb","watermalon")
	print (re.rstrip())

'''

n = input().strip()
print (n)
print (len(n))
print (type(n))

nn = input().split()
print (nn)
print (len(nn))
print (type(n))
