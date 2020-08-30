
n = int(input("Number of states : "))

d={}

for i in range(n):
	name = input().split()
	key = name[0]
	#print (key)
	values = name[1:]
	#print (values)
	d[key]=values

for k,v in d.items():
	print (k,v)

print ("---------")

#dd = {city:state for state,city in d}


'''
dd={}
for state,s in d.items():
	for town in s:
		dd[town]=state
		
print (dd)
'''

ddd = {town:state for state,city in d.items() for town in city}
#ddd = {city:state for state,cit in d.items() for city in cit}
print (ddd)

