
import sys

for word in sys.stdin.read().split() :
	word_T = word.upper()
	#if "bomb" in word.upper()
	ans = word_T.find("BOMB")
	if ans!=-1:
		print ("YES")
		break
else:
	print ("NO")