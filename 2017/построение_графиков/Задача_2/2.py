

# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

fig,ax1=plt.subplots(figsize=(12,6))


t=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
T=[-8,-9,-9,-11,-12,-12,-12,-12,-11,-9,-8,-7,-7,-6,-6,-5,-4,-4,-4,-4,-3,-3]
H=[86,87,89,90,89,87,88,86,85,82,80,81,82,84,84,85,85,86,85,86,88,89]

#ax1.set_title("Temp (C) and Humidity (%) forecast", fontsize=16)
ax1.set_xlabel("Time", fontsize=14)

ax1.plot(t,T, 'bo', t, T)
ax1.axis('tight')

ax1.set_ylabel("Temp (C)", fontsize=16, color="blue")

plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],['02am','','04am','','06am','','08am','','10am','','12pm','','02pm','','04pm','','06pm','','08pm','','10pm'])


for name in ax1.get_yticklabels():
	name.set_color("blue")
	
ax2=ax1.twinx()
ax2.plot(t, H, 'rs', t, H,'r', color="red")
ax2.set_ylabel("Humidity (%)", fontsize=16, color="red")
ax2.axis('tight')

for name1 in ax2.get_yticklabels():
	name1.set_color("red")

for namex in ax1.get_xticklabels():
	namex.set_color("yellow")
	
ax1.set_title("default grid")
plt.show()
fig.savefig('2.png')
