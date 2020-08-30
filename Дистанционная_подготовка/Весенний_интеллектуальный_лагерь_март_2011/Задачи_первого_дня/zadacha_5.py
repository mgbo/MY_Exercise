

d = int(input("Номер дня недели : "))
n = int(input("Номер урока в этом дне : "))

def total_lesson(d, n):
	t_lesson = (d-1)*6 + n
	return t_lesson

print (total_lesson(d, n))