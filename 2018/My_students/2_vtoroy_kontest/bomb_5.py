
import sys
count = 0

ans_w = []
for word in sys.stdin :

	n_word = word.replace("bomb","watermelon")


	#print (n_word.rstrip())# убирать личный \n
	print (n_word,end='')