

(price,delta,money)=map(int,input().split())


i=1
week_day = 1


while money>=price:
	money=money-price
	print ("i=%d money=%d"% (i, money))
	i=i+1
	week_day += 1
	#print "money=%d"% money
	if week_day == 8:
		week_day = 1
		price=price+delta
		print ("price=%d "% price)


print (i-1)
