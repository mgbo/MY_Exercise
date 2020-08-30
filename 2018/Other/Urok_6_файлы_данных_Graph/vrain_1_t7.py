
f = open("tr_test.log",'r')

max_login=2

for line in f:
	s_line = line.split()

	if not s_line:
		break

	name_deysviya = s_line[2]
	#print ("Имя действия : ",name_deysviya)

	if name_deysviya!="login":
		continue
	max_login = max(max_login,float(s_line[3]))
	print ("s_line : ",s_line[3])


print (max_login)

f.close()
