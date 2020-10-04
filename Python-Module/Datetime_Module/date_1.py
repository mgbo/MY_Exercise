

import datetime

'''
print('---- datetime.date() -------------') # year, minutes, days ကိုတွက်ချက်တဲ့အခါသုံး
d = datetime.date(2020, 5, 1)
print (d, type(d))


today = datetime.date.today()
print (today, type(today))
print (today.weekday()) # weekday မှာ ဆိုရင် Mondalay က 0 Sunday က 6 အစဉ်တိုင်းသွား
print (today.isoweekday()) # weekday မှာ ဆိုရင် Mondalay က 1 Sunday က 7 အစဉ်တိုင်းသွား


print ("\n-------- datetime.timedelta -------")
tdelta = datetime.timedelta(days=7)
print(tdelta)
print (tdelta + today) # 7 ရက်တိုးကြည့်တာ
print (today - tdelta)


# မွေးနေ့ ကနေ ယခု အချိန်ထိ second ဘယ်လောက်ကုန်လွန်သွားတာလဲ ထွက်
bday = datetime.date(1991, 3, 28)
print (bday)
till_bday = bday - today
print (till_bday, till_bday.total_seconds())
'''

print ("----- datetime.time() ------") # hours, minutes, seconds and microseconds တွေကိုတွက်ချက်တဲ့အခါမှာ အသုံးပြု
t = datetime.time(9, 30, 45, 100000) 
print(t.hour)


print ("\n------ datetime.datetime()------------") # years, months, day, hours, minutes, seconds, microsecond 

dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 10000)
# print (dt, dt.year)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_now)
print(dt_now);
print(dt_utcnow)


















