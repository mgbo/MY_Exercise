

d = {}

with open('file_AD.txt', 'r') as f:
	for i in f:
		i_s = i.strip()
		if i_s not in  ('PARTIES:','VOTES:'):
			if i_s in d:
				d[i_s]+=1
			else:
				d[i_s] = d.get(i_s,1)

list_d = [p for p in d.items()] # convert from dit to list
print (" list_vote : ",list_d)

# ----------- for sort max_values and name ---------
def sot(dv):
	p,v = dv
	#print(p,v)

	vu = -v
	return vu,p

list_d.sort(key=sot)# sort using function sot


for i in range(len(list_d)):
	print (list_d[i][0])

f.close()



'''
d={0: 10, 1: 20,3:40,4:5}
x = [(i,d[i]) for i in sorted(d, key=d.get)]

y = [(i,d[i]) for i in sorted(d, key=d.get, reverse=True)]
print(x)
print(y)
'''

# ------------- good idea -----------------
'''
d = {1: 2, 
	3: 4,
	4: 3,
	2: 1,
	0: 0}

sorted_list = [x for x in d.items()] # tuple in list  
print ("fist : ",sorted_list) #[(1, 2), (3, 4), (4, 3), (2, 1), (0, 0)]


sorted_list.sort(key=lambda x: x[0]) #sort by key
sorted_list.sort(key=lambda x: x[1]) #sort by value

print("Sorted by Value Ascending:",sorted_list)
sorted_list.reverse()
print("Sorted by Value Descending",sorted_list)

'''







