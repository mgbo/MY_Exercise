
import sys

"""
# example использование update
Days = {
    'Sunday': 0,
    'Monday': 1,
    'Tuesday': 2,
    'Wednessday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6
}

name = {
	'chit': 1500,
	'ko': 1000
}

name.update(Days) #объединение dict name and Days

print (name)
"""
d = dict()

for imf in sys.stdin:
	key, *value = imf.split()
	if key in d:
		d[key].append(value)
	else:
		d[key] = [value]

for key, value in sorted(d.items()):
	#print (key,value)
	print (key + ":")
	a = int(value[0][1])
	#print (a)

	value1 = {}
	s = {}

	for val in value:
		value1[val[0]] = val[1]
		if val[0] in s.keys():
			s[val[0]] = val[1]
			a = int(a) + int(val[1])
			s[val[0]] = a
			value1.update(s)
		else:
			s[val[0]] = val[1]
			value1[val[0]] = val[1]
            
	for key in sorted(value1.keys()):
		print(key, end=" ")
		print(value1[key])

