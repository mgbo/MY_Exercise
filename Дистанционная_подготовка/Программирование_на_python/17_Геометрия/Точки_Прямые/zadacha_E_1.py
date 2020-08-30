
x1, y1, x2, y2 = map(int, input().split())

x3, y3, x4, y4 = map(int, input().split())


def Orientation(x1, y1, x2, y2, x3, y3):
	v = (y2 - y1) * (x3 - x2) - (x2 - x1) * (y3 - y2)
	print ("v ---> {}".format(v))
	if v == 0:
		# print ("Коллинеарны")
		return 0

	elif v >  0:
		# print ("Clock wise")
		return 1

	else:
		# print ("CounterClock wise")
		return 2

ans = Orientation(x1, y1, x2, y2, x3, y3)
print (ans)


def CheckIntersect(x1, y1, x2, y2, x3, y3, x4, y4):
	# Find the four orientation needed or general and special cases
	o_1 = orientation(x1, y1, x2, y2, x3, y3)
	o_2 = orientation(x1, y1, x2, y2, x4, y4)
	o_3 = orientation(x3, y3, x4, y4, x1, y1)
	o_4 = orientation(x3, y3, x4, y4, x2, y2)

	print ('o_1 : {} , o_2 : {} , o_3 : {}, o_4 : {}'.format(o_1, o_2, o_3, o_4))

	if o_1 != o_2 and o_3 != o_4:
		return True

	else:
		return False



if CheckIntersect:
	print ("YES")

















