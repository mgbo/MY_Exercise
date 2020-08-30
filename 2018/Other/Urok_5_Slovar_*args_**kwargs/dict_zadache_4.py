
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
dd={}


for state,s in d.items():
	for town in s:
		dd[town]=state
		
print (dd)


nn = int(input("Number of city : "))
for y in range(nn):
	name_city = input()
	if name_city in dd.keys():
		print (dd[name_city])
