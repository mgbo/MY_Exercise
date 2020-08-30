
txt = input()

new = ''

for t in txt.split():
	new += t[0].upper() + t[1:].lower() + ' '

print (new.rstrip())

