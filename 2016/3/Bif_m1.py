
(h,m)=map(int,raw_input().split())

time=h*60+m


if  0<=time and 359>=time:
	print "DARK"
	


if 360<=time and time<=719:
	print "LIGHT"
	

if 720<=time and time<=1079:
	print "LIGHT"
	
	
if 1080<=time and time<=1439:
	print "DARK"
	
#321>=time and time<=1440 or

	
	
