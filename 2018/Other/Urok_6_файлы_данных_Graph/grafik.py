
# ПРИМЕР 

import matplotlib.pyplot as plt
import numpy as np

x = [0,1,2,3,4,5,6,7,8,9,10]
y = [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11]

fig = plt.figure()

# первая область рисования
ax = fig.add_subplot(211)
line = ax.plot(x,y,'-',color='blue',linewidth=2)
print ("Lines on the axes:",type(line),line)

# Вторая область
ax2 = fig.add_subplot(212)
n,bins,rectangles = ax2.hist(np.random.randn(1000),50,facecolor='yellow')
print ("Patches on the axes : ",len(ax2.patches),rectangles)

for ax in fig.axes:
	ax.grid(True)

#save('pic_1',fmt='png')
#save('pic_2',fmt='pdf')

plt.show()
