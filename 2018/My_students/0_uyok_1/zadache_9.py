
# -*- coding: utf-8 -*-
L = int(input())      # пробежал в первый день
k = int(input())      # завтра пробежит на k метров больше

                      # Готовимся бегать
day = 0               # всего пробежал 0 дней
total = 0             # еще не бегал         
sday = L              # побежит в первый день L метров

                      # побежали
while day < 4:               # пока прошло меньше 4 дней
    total = total + sday     # к общему результату добавь сколько бегал сегодня
    day = day + 1            # день закончился   
    print("за day=%d дней пробежал total = %d" % (day, total))
                             # готовимся к завтрашнему дню
    sday = sday + k          # завтра пробежит на k больше
    print("sday = %d" % (sday))

                      # цикл закончился
print(total)          # после цикла (1 раз) напечатать сколько всего пробежал
