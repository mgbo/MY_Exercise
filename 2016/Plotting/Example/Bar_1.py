
import numpy as np
import matplotlib.pyplot as plt

objects=('A','B','C','D','E','F','E')

y_pos=np.arange(len(objects))

performance=[10,8,4,6,2,1,3]

plt.bar(y_pos,performance,align='center',alpha=.5)

plt.xticks(y_pos,objects)

plt.show()

