
def chek_skobki(o,c):
	if o=="(" and c==")":
		#print (o,c)
		return 1

	elif o=="<" and c==">":
		#print (o,c)
		return 1

	elif o=="{" and c=="}":
		#print (o,c)
		return 1

	elif o=="[" and c=="]":
		#print (o,c)
		return 1
	else:
		return 0


def chek(l):
	new = []
	for n in l:
		if n in "(<{[":
			new.append(n)
			#print (new)
			#lenn = len(new)
			#print (lenn)

		elif n in ")>}]":
			if not new:
				print ("NO")
				break
			a = new.pop()

			if chek_skobki(a,n) != 1:
				print ("NO")
				break
	else:
		lenn = len(new)
		if lenn>0:
			print ("NO")
		else:
			print ("YES")

skobki = input()
chek(skobki)









