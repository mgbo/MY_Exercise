
# ------------ v1 ------------------
'''
a = input().split()
print (a)
print(' '.join([x for x in a if x != '0']+['0']*a.count('0')))
'''

#--------------- v2 -----------------

a = input().split()
b = [x for x in a if x != '0']
# print (b)

b.extend(x for x in a if x == '0')

# print (b)

print(' '.join(b))