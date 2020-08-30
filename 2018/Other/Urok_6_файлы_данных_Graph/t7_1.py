
f = open("tr_test.log",'r')


time_login = []
max_login = 1

for line in f:
	s_line = line.split()
	value = s_line[2] # имя действии 
	if value != 'login':
		continue
	max_login = max(max_login, float(s_line[3]))
	#time_login.append(float(s_line[3])) # длительность действии
	#d[key]=value

print(min(max_login))

'''
for k,v in d.items():
	print ("%s:%s"%(k,v))

N_dlitelna = []

Name_deystviya = input('Write of name of action :')
for k in d:
	if Name_deystviya in d[k]:# если N в значении 
		N_dlitelna.append(k)
	
print ("\n------------")
print (N_dlitelna,'\n')

print ("Максимальная длитеность действия {} : {} second ".format(Name_deystviya,max(N_dlitelna)))
'''
f.close()
