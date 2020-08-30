
L,k = map(int,input().split())

path = 0
step = L
i = 0

def nextStep(step,k):
	step = step - k
	if step < 0:
		step = 0
	return step

while step > 0:
	path = path + step
	i+=1
	#print ("Number ({}) of step and Total Path {} ".format(i,path))
	step = nextStep(step,k)
	#print ("For next day : {}".format(step))

print (path)
print (i)

	