
'''

Количество слов

'''

line = input()

def CountWord(s):
	count = 0
	expr = line.split()
	for i in expr:
		# print (i)
		# print (type(i))

		if ',' in i:
			print (i)
			print ('FOUND')
			
			count +=1
		# ind = i.find(',')
		# print (ind)
		# print ("В этом слове содержил запятая : {} ".foramt(i))
		count +=1
	return count

ans = CountWord(line)
print (ans)