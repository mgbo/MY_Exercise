
# ------------ List -------------------

li = [9,1,8,2,7,-3,6,4,5]

s_li = sorted(li, key=abs, reverse = True)

print (li)
print ('Sorted Variable :\t',s_li)

li.sort(reverse = True)

print ('Sorted Variable :\t',li)

# --------------- Tuples ----------------
tup = (9,1,8,2,4,2,1,9,77)

s_tup = sorted(tup)

print (tup)
print ('Sorted Variable :\t',s_tup)

# -------------- dictionary -------------

di = {'name':'Corey','job':'programming','age':None, 'os':'Mac'}

s_di = sorted(di)
print ('Sorted Variable :\t',s_di)







