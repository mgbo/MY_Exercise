
dis = int(input())
step = int(input())

i=0
ostatok=dis

while ostatok>step:
	ostatok = ostatok - step
	i = i + 1

print (ostatok)
print (i)