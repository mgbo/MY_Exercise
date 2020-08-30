

f = open("tr_test.log",'r')

time_login = []

for line in f:
	s_line = line.split()
	value = s_line[2] # имя действии 

	if value != 'login':
		continue
	time_login.append(float(s_line[3])) # длительность действии

print (time_login)

print(min(time_login))
