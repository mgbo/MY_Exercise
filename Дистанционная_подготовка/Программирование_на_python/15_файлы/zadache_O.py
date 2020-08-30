
d = {}
list_mark = []
count =1

with open ('file_O.txt', 'r') as f:
	for i in f:
		s_i = i.split()
		name = s_i[:2]
		full_name = ' '.join(name)
		#print (full_name)

		mark = int(s_i[-1])

		list_mark.append(mark)

		m = list_mark[0]

		if m<mark:
			m = mark
			# print (full_name)
			winner = full_name

print (winner)
		
f.close()


