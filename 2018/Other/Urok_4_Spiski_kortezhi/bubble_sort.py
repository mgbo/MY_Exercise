
n = [10,75,43,15,25,-4,27]

print (len(n))

def bubble_sort(mylist):
	last_item = len(mylist)-1
	for x in range(0,last_item):
		for z in range(0,last_item-x):
			print (mylist)
			if mylist[z]>mylist[z+1]:
				mylist[z],mylist[z+1] = mylist[z+1],mylist[z]
	return mylist

print ("old list : ",n)

new_n = bubble_sort(n).copy()

print (new_n)
