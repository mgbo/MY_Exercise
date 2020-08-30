

nums = [1,2,3,4]

squares = [n*n for n in nums]

print (nums)
print (squares)

strs = ['hello','and','goodbye']

shouting = [n.upper()+'!!!' for n in strs]
print (strs)
print (shouting)

## Select values <=2
numss = [1,-1,-8,9,19,2]

ans_num = [n for n in numss if n<=2]
print (ans_num)


##Select fruits containing 'a'

fruits = ['apple','cherry','bannana','lemon']
afruits = [s.upper() for s in fruits if 'a' in s]
print (afruits)


