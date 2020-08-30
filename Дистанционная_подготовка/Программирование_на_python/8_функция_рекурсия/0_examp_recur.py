
def sum(x):
	if x == 0:
		return 0
	elif x == 1:
		return 1
	else:
		print ("{} + {} = {}".format(x,sum(x-1),x+sum(x-1)))
		return x + sum(x-1)

s = sum(5) #0+1+2+3+4+5
print (s)