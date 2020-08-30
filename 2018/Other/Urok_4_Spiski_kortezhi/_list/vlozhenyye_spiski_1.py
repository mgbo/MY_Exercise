
## primer_1
a = []
for x in range(1,5):
	print (x)
	a.append(x**2)

print (a)

# если функция достаточно сложная, можно ее написать отдельно

def sqr(x):
	return x**2

a = list(map(sqr,range(1,5)))
print ("a is : ",a)

## For example
m = [(x,y) for x in [1,2,3] for y in[3,1,4] if x!=y]
print (m)

##---- то же самое -----------
combs = []

for x in [1,2,3]:
	for y in [3,1,4]:
		if x!=y:
			combs.append((x,y))

print (combs)










