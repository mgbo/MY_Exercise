
first_day = int(input())
max_kilo = int(input())

day = 1
s_day = first_day # for second day 
total = 0

while s_day<max_kilo:
	total = total + s_day
	# print ("day {} ,first_day for per {}".format(day,s_day))
	s_day= s_day*1.1
	day +=1
	# print ("day {} ,first_day for per {}".format(day,s_day))

# не менее y километров
print (day)