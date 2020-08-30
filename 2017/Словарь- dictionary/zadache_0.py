
# -*- coding: utf-8 -*-
nn = input()
#print "nn : ", nn ,"\nlen nn :", len(nn)

without_sp = map(int,nn.split())

final_number = set(without_sp)
print ("final nuber : ", final_number)

print (len(final_number))
