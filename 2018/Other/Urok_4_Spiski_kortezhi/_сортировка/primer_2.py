
# Say we have a list of strings we want to sort by the last letter of the string

strs = ['xc','zb','yd','wa']

# write a little function that takes a string,and returns its last letter

def Myfn(s):
	return s[-1]

print ("string :",Myfn(strs))
print (sorted(strs,key=Myfn))
