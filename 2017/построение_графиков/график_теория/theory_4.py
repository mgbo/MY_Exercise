
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

fig,ax1 = plt.subplots(figsize=(8,5))

r = np.linspace(0,5,100)
a = 4 * np.pi * r**2 # area
v = (4 * np.pi/3) * r**3 # volume

ax1.set_title("surface area and volume of sphere", fontsize=16)

ax1.set_xlabel("radius[m]", fontsize=16)
ax1.set_ylabel(r"surface area($m^2$)", fontsize=16, color="blue")

ax1.plot(r, a, color="blue")

for label in ax1.get_yticklabels():
	label.set_color("blue")
	
ax2=ax1.twinx()

ax2.plot(r, v, color="red")

ax2.set_ylabel(r"volume($m^3$)", fontsize=16, color="red")

for label in ax2.get_yticklabels():
	label.set_color("red")
	
plt.grid(True)
plt.show()


 
