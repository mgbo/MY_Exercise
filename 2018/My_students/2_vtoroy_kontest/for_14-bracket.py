
line = input()

count = 0

for x in line:
	if count==-1:
		break
	elif x=='(':
		count = count + 1
	elif x==')':
		count = count - 1


if count==0:
	print ("YES")
else:
	print ("NO")
