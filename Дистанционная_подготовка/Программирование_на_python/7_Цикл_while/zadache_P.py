

max_n = 0


while True:
	n = int(input())
	if n>0:
		if n>max_n:
			max_n=n
			count = 1
			print ("max : ",max_n)
		elif max_n==n:
			count+=1
			print ("count : ",count)
	else:
		break

print (max_n)
print (count)


'''

maximum = 0
num_maximal = 0
element = -1

while element != 0:
    element = int(input())
    if element > maximum:
        maximum, num_maximal = element, 1
        print ("Max {} --> num_maximal {}".format(element,1))
    elif element == maximum:
        num_maximal += 1
        print ("count : ",num_maximal)
print(num_maximal)

'''








