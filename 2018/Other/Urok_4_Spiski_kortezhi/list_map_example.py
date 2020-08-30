
n = [[1,2,3,4],[5,6,7,10],[1,2,4],[1,2]]

print (n)

'''
for i in n:
	for ii in i:
		print (ii)
'''

nn = [xx for x in n for xx in x]
print (nn) 
print (type(nn))

