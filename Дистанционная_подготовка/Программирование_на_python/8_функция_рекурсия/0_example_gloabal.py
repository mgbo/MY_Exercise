
"""
Локальные и глобальные переменные
"""

def f():
	# print ("переменные --> ".format(a))
	print (a)

a = 1
f() # 1
print ('-------')

a = 5
f() # 5

def f():
	a = 1
	print(a)
a = 0
f() #1
print(a)# 0


def f():
    global a
    a = 1
    print (a)
a = 0

f()# 1
print(a)#1









