
p_x, p_y, x, y, x1, y1,  = map(float, input().split())

def Crossproduct(p_x, p_y, x1, y1, x2, y2):

	cr_p = (y2 - y1) * (p_y - y) - (p_x - x2) * (p_y - y2)
	return cr_p


def CheckBelong(p_x, p_y, x1, y1, x2, y2):

	k_ac = Crossproduct(x1, y1, x2, y2, p_x, p_y)
	k_ab = Crossproduct(x1, y1, x2, y2, x2, y2)

	print (k_ac, k_ab)

	if 0< k_ac < k_ab:
		t = True

	else:
		t = False

if CheckBelong(p_x, p_y, x, y, x1, y1):
	print ("YES")

else:
	print ("NO")
