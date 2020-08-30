
# -*- coding: utf-8 -*-
'''
x = raw_input()
b = "."

c = b.join(x)
print c

a = "hel"
b = "lo"
print (a+b)
print (len(a+b))
'''
l = input()

con = l.count("h")
print (con)

con1 = l.startswith("ch")
print (con1)

con2 = l in "he"
print (con2)

con3 = l.find("s") # первое вхождение 
print (con3)

con4 = l.rfind("s")
print (con4)

a= input()
print (a)
print ('.'.join(a))

print ("-----")

line = input()
pair = line.split()
print (pair[0])
print (pair[1])




