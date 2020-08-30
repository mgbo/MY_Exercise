
# -*- coding: utf-8 -*-
L = int(input())      # пробежал в первый день
k = int(input())      # завтра пробежит на k метров больше
total = int(input())
                      # Готовимся бегать
day = 0               # всего пробежал 0 дней
             # еще не бегал         
sday = L              # побежит в первый день L метров


while total>0:
	total = total - sday
	day = day + 1
	
	print("за day=%d дней пробежал total = %d" % (day, total))
	

	sday = sday + k
	
	print ("sday = %d" %(sday))

print ("DAY :",day)
