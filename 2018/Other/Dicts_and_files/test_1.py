
dict = {}

dict['a'] = 'alpha'
dict['b'] = 'beta'
dict['g'] = 'gamma'
dict['o'] = 'omega'
dict['1'] = '7'

print (dict['a'])

dict['a']=6

print ('a' in dict)

'''
if 'z' in dict:
	print (dict['z'])
	print dict.get('z')
'''
for key in dict:
	print (key)

for key in dict.keys():
	print (key)
print ('\n')

for values in dict.values():
	print (values)


for key in sorted(dict.keys()):
	print (key,dict[key])

for k,v in dict.items():
	print (k,'>',v)


#---------------- Dict formatting --------------

hash = {}
hash['word']='garfield'
hash['count']=42

s='I want %(count)d copies of %(word)s' %hash

print (s)





