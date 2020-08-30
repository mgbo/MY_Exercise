
import turtle

def stare(t,x,ang):
	
	
	t.fd(x)
	t.rt(ang)
	
	t.fd(x)
	t.rt(ang)
	
	t.fd(x)
	t.rt(ang)
	
	t.fd(x)
	t.rt(ang)
	
	t.fd(x)
	t.rt(ang)
	
mp=turtle.Turtle()

mp.speed(6)
mp.width(5)
mp.hideturtle()
stare(mp,150,144)

#mp.fd(150)


turtle.mainloop()
