
# Преамбула

%matplotlib inline

import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

def save(name='', fmt='png'):
    pwd = os.getcwd()
    os.chdir('./pictures/%s' % fmt)
    plt.savefig('%s.%s' % (name, fmt), fmt='png')
    os.chdir(pwd)

rcParams['font.family'] = 'fantasy'
rcParams['font.fantasy'] = 'Arial'
