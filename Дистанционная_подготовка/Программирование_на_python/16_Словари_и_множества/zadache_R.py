
import sys

d ={}
register_user = set()

for l in sys.stdin:
	l_s = l.split()

	#-------------  'DEPOSIT' --------------
	if l_s[0] == 'DEPOSIT':
		user = l_s[1]
		amount = l_s[2]
		if user not in d:
			d[user]=int(amount)
			register_user.add(user)
		else:
			d[user]+=int(amount)

	#-------------  'WITHDRAW'--------------
	if l_s[0]== 'WITHDRAW':
		d[l_s[1]]=d.get(l_s[1],0)-int(l_s[2])
		register_user.add(l_s[1])

	#-------------  "BALANCE" --------------
	if l_s[0] == "BALANCE":
		if l_s[1] not in d:
			print ('ERROR '+'потому что у "{}" нет account '.format(str(l_s[1])))
		else:
			print(l_s[1],d[l_s[1]])

	#-------------  'TRANSFER' --------------
	if l_s[0] == 'TRANSFER':
		if d[l_s[1]]>=int(l_s[3]):
			d[l_s[1]]-=int(l_s[3])
			if l_s[2] not in d:
				d[l_s[2]]=int(l_s[3])
				register_user.add(l_s[2])
			else:
				d[l_s[2]]+=int(l_s[3])
		else:
			print ("Денги не хватает на перевод")

	# --------------- 'INCOME' -------------------
	if l_s[0] == 'INCOME':
		for usar in register_user:
			d[usar] = d[usar]+ int(l_s[1])
			#print ("CHECK : ",usar,d[usar])

print (register_user)
	
	



