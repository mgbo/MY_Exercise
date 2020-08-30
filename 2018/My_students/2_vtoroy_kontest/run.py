
l = int(input())
k = int(input())

sday=l
day=0
total=0

while day<20:
	total = total + sday
	day+=1
	print ("day {} , {} meter and total {}".format(day,sday,total))
	sday=sday+k

print (total)
