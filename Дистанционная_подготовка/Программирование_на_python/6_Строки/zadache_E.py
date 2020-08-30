
s = input()

l =[]
c = 0

for i in s:

	if i.lower()=="f":
		l.append(c)
	c+=1

print (*l)