
'''

сумма факториалов


'''

n = int(input())

sumn = 1
ans = 0
for i in range(1,n+1):
	sumn*= i
	# print ("Sumn {} --> {}".format(i,sumn))
	ans +=sumn

print (ans)
	
