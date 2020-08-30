
import random
import math
import datetime
import calendar
import os


courses = ['History','Math','Physics','ComSci'] 

random_course = random.choice(courses)
print (random_course)

rads = math.radians(45)
print (math.sin(rads))

today = datetime.date.today()
print (today)

print (calendar.isleap(2017))


print (os.getcwd())

print (os.__file__)





