
with open ('file_i.txt', 'r') as f:

	for st in f:
		#print (st)
		#print (type(st))
		for num in st:
			if num in "0123456789":
				print (num)


'''
total = 0

with open('file_i.txt', 'r') as inp, open('output.txt', 'w') as outp:

   for line in inp:
       try:
           num = float(line)
           total += num
           outp.write(line)

       except ValueError:
           print('{} is not a number!'.format(line))

print('Total of all numbers: {}'.format(total))
'''