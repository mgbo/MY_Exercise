
# -*- coding: utf-8 -*-
L = int(input())      # пробежал в первый день
k = int(input())      # завтра пробежит на k метров больше
n = int(input("day : "))
                      # Готовимся бегать
day = 0               # всего пробежал 0 дней
total = 0             # еще не бегал         
sday = L              # побежит в первый день L метров



while sday>0:
	
	total = total + sday
	day = day + 1
	print("за day=%d дней пробежал total = %d" % (day, total))
	
	if sday>=k:
		sday = sday - k
		print ("Next_day = %d" %(sday))
	else:
		break

print ("Total Day : ",day)
