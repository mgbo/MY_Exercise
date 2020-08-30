
s = input()

l =[]
c = 0

for i in s:

	if i.lower()=="f":
		l.append(c)
	c+=1


if len(l) == 1:
	print (-1)

elif len(l) > 1:
	print (l[1])

else:
	print (-2)