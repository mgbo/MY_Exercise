
n = int(input("Количество страниц : "))

total = 0
day = 1
f = 1
s = 0

while total<n:
	f,s = s,f+s
	print (s)
	total+=s
	print ("day : {} ,total : {} ".format(day,total))
	day+=1


print ("day : ",day-1)






