

numbers = [int(s) for s in input().split()]

#print (numbers)

occur_before = set()

#print (occur_before)

for num in numbers:
	if num in occur_before:
		print ("YES")
	else:
		print ("NO")
		occur_before.add(num) # add function only for set()

		
"""
n = set()

nn = int(input())

n.add(nn)

print (n)

"""


