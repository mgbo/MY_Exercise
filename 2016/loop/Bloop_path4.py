# -*- coding: utf-8 -*-

# функция nextStep уменьшает шаг и возвращает новый шаг
def nextStep(step, k) :
    step = step - k
    if step < 0 :
        step = 0
    return step;
    
# читаем входные данные
# L - длина первого шага
# k - на сколько уменьшить шаг
(L, k) = map(int, raw_input().split())

# готовимся делать шаги
i = 0       # сколько шагов уже сделали, сначала шагов 0
step = L    # длина шага, сюда записать размер первого шага
path = 0    # сколько всего прошли, сначала прошли 0


while step > 0 :                    # Считаем шаги и проверяем шаг (>0)
    path = path + step;             # робот сделал шаг
    #print "path = %d " % path
    
                                    # готовимся к следующему шагу
    # функция nextStep уменьшает шаг и присваивает это число step
    step = nextStep(step,k);        # шаг уменьшился
   # print "step = %d " % step
    i=i+1

print path                          # печатаем путь
print i
