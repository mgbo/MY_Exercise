
unconfirmed_user = ['alice','brain','candace','chit']
confirmed_users = []

i = 0
while unconfirmed_user:
	current_user = unconfirmed_user.pop()

	print ("Verifying user : "+current_user.title())
	confirmed_users.append(current_user)
	i+=1

print (i)

for confirmed_user in confirmed_users:
	print (confirmed_user.title())