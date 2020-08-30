
import numpy as np
import matplotlib.pyplot as plt

f = open("bet.log",'r')
d = {}

for line in f:
	s_line = line.split()
	deystviya = s_line[1]
	# хочу узнать сколько раз покупатели купили по одному
	d[deystviya]=d.get(deystviya,0)+1

for k,v in d.items():
	print (k,v)

print ("len : ",len(d))

koli_zap = []

for i in d.values():
	koli_zap.append(i)

print ("koli : ",koli_zap)

width = 1/1.5
#x = range(len(d))
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

p1 = plt.bar(x,koli_zap,width,color="blue")

plt.xticks(np.arange(1,16,1))
plt.yticks(np.arange(0,81,5))

plt.show()

f.close()




