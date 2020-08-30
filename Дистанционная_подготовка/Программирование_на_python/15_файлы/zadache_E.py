
with open('file_D.txt', 'r') as f:
	s = f.readlines()
	#print (s)
	#print (type(s))  

	'''
	['Beautiful is better than ugly.\n', 
	'Explicit is better than implicit.\n', 
	'Simple is better than complex.\n', 
	'Complex is better than complicated.\n']
	'''

	for line in s[::-1]:
		print (line[::-1].strip())

