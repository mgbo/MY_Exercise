
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

time=[]
note=[]

readfile=open('tr.log','r')

sepfile=readfile.read().split('\n')
print ("sepfile : ",sepfile)
readfile.close()

for line in sepfile:
	#print line
	a = line.split()
	#print (a)
	if not a:
		break
		
	time.append(a[0])
	note.append(a[3])


#print ("Time : ",time)
#print ("Note : ",note)

numNote = len(note)
#print ("колечество записей : ",numNote)

#sepfile=readfile.read().split('\n')
#print sepfile

plt.plot(time,note,'ro')

plt.title('matplotlib title')
plt.xlabel('matplot Time label')
plt.ylabel('matplot Note label')
plt.grid(True)

plt.show()
