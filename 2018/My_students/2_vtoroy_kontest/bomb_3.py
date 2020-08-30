
import sys

for word in sys.stdin:
	word.upper()
	print (word)
	ans = word.find("bomb")
	if ans != -1:
		print ("YES")
		break

else:
	print ("NO")