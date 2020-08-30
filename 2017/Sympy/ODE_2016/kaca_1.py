
# -*- coding:utf-8-*-

import sympy as sm
from sympy.plotting import plot
import matplotlib.pyplot as plt
import numpy as np
from sympy import* # для pprint
x = sm.Symbol('x')

f = sm.S('1/2')*x**2

print ("equation :")
pprint (f) # если используются pprint(), нужно писать from sympy import*
print "-------"
df = f.diff(x)
print df

# x0= 1

T_1 = f.subs({x:1})+df.subs({x:1})*(x-1)

print "tangent : "
print T_1


print(T_1.subs({x:1})==f.subs({x:1}))# только проверка

a = np.arange(0,3.01,0.01)
plt.plot(0.5*a**2,a,'r',a-0.5,a,'b')


plt.grid(True)
plt.show()

plot (f,T_1,(x,0,3))



