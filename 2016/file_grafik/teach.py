'''
al=[1,1,1,2,3,5,8,0,9,10]
print al

sl=set(al)

print sl

ul=[]


for x in al:
	
 if not x in al:
	ul.append(x)
	print ul
  
print '------'
print ul
'''

d={'russia':'Moscow','india':'New delhi'}
print (d)

d['Myanmar ']='NayPyiTaw'
print (d)

d['Mongolia']='Ulaan Baator'
print (d)

d['Mongolia']='Ulaanbaatar'
print (d)

print (d['russia'])

print ('----------------')

for state in sorted(d.keys()):
	print (state,d[state])

print ('________________')

for town in d.values():
	print (town)

print ('\n\n\n--------')


