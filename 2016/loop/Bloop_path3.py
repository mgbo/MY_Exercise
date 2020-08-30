
# -*- coding: utf-8 -*-

def nextStep(step, k) :
    step = step - k
    if step < 0 :
        step = 0
    return step;

# читаем входные данные
# L - длина первого шага
# k - на сколько уменьшить шаг

(l,k)=map(int,raw_input().split())

i=0
step=l
path=0


while i<20:
	path=path+step;
	#print "step =%d" % step
	i=i+1
	# функция nextStep уменьшает шаг и присваивает это число step
	step=nextStep(step,k);
	#print "step =%d" % step
	
	

print path
