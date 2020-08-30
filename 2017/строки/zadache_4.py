
# -*- coding:utf-8 -*-

l = input()
#l = "aahhhhhbb"
print (len(l))
i = l.index('h')
#print i

fl = l[:i+1]
print (fl)

f = l.rfind("h")
print (f)

ml = l[i+1:f]
print (ml)

r = ml.replace('h','H')
#print r

ll = l[f::]

print (fl+r+ll)
print(len(fl+r+ll))



