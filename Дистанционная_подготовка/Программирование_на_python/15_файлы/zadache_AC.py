
l = []

with open('file_AC.txt', 'r') as f:
	for i in f:
		i_s = i.strip()
		#print (i_s)
		#print (type(i_s))

		if i_s not in  ('PARTIES:','VOTES:'):
			l.append(i_s)

s = set(l)
print (s)

votes = len(l) - len(s)
print (votes)

for p in s:
	coun = l[3:].count(p)
	#print ("Parter Name : {} , Votes number : {}".format(p,coun))

	if coun/votes >=0.08:
		print (p)


f.close()


'''

f_l = [l for l in map(str.strip, open('file_AC.txt')) if l not in ('PARTIES:', 'VOTES:')]

print (len(f_l))
print (f_l)

for let in f_l:
	print (let)
'''





