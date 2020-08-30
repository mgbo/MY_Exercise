
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


