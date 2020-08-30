
import numpy as np
import matplotlib.pyplot as plt

f = open("bet.log",'r')
d = {}

for line in f:
	s_line = line.split()
	nomer_kliyan = int(s_line[1])
	d[nomer_kliyan]=d.get(nomer_kliyan,0)+1 # хочу узнать сколько раз покупатели купили по одному

for k,v in d.items():
	print (k,v)

num_cus = sorted(d.keys())
print ("Номер покупателя : ", num_cus)

width = 1/1.5
#x = range(len(d))

x = [i+1 for i in range(len(num_cus))]
y = [d[uid] for uid in num_cus]


#p1 = plt.bar(range(len(d)),d.values(),width,color="blue")
p1 = plt.bar(x, y, width, color="blue")

plt.xticks(np.arange(1,16,1))
plt.yticks(np.arange(0,81,5))

plt.show()

f.close()




