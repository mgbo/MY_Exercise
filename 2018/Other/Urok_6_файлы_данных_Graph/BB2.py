#-*- coding:utf-8 -*-

# Количество записей от времени(в минуту)
import matplotlib.pyplot as plt
import numpy as np

time = []
kolichestbo = []
t_start = 0
i = 0
interval = 360

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
f.close()

#print ("------------------- Graph -------------------------")


fig = plt.figure(figsize=(12,5))

width=1

p1 =plt.bar(time,kolichestbo,width,color='blue')

plt.title("Graph")
plt.xlabel('time')
plt.ylabel('kilichestbo')

#plt.grid(True)

plt.xticks(np.arange(1,600,50))
plt.yticks(np.arange(0,13,1))

plt.show()
