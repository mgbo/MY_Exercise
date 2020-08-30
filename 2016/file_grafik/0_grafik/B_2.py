
#-*- coding:utf-8 -*-

# Количество записей от времени(в минуту)
import matplotlib.pyplot as plt

time = []
kolichestbo = []
t_start = 0
i = 0
interval = 60

f = open ('bet.log','r')

for line in f:
	sl = list(map(int,line.split()))
	if not sl:
		break
	if t_start == 0:
		t_start = sl[0]
		print ("start : ",t_start)
	n = (sl[0] - t_start)/interval
	print (i,n)

	if n*interval in time:
		kolichestbo[i-1] = kolichestbo[i-1] + 1
	else:
		time.append(n*interval)
		kolichestbo.append(1)
		i+=1

print ("Time : ",time)
print ("kolichestbo : ",kolichestbo)
#print ("-------------")
f.close()

plt.plot(time,kolichestbo,'bo')
plt.title("Graph")
plt.xlabel('time')
plt.ylabel('kilichestbo')
#plt.grid(True)
plt.show()











