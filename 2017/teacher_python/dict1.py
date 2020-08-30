d = {
	'Russia': 'Moscow', 
	'Ukraine': 'Kiev', 
	'USA': 'Washington',
	'Myanmar':'Naypyidaw', 
	'Mongolia':'Ulaanbaatar', 
	'China':'Beijing'
}

#print (d)
for state in d.keys():
	print(state, d[state])
print('----')

for town in d.values():
	print(town)
print('=====')

for k, v in d.items():
	print(k, v)

