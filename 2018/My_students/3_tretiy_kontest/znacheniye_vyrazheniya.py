
'''
Дана строка, состоящая из n цифр (т.е. однозначных чисел),
между которыми стоит n−1 знак операции, каждый из которых
может быть либо +, либо -. Вычислите значение данного выражения.

Решение оформите в виде функции Evaluate(S), где S - строка с выражением,
а возвращаемое значение функции - результат вычисления этого выражения.

'''
def cal_1(n):
	new = []

	for i in n:
		if i in "0123456789":
			new.append(i)

	for i in n:
		if i in "+":
			#print (new)
			s = new.pop(1)
			f = new.pop(0)
			#print ("+ : ",s,f)
			new.insert(0,int(f) + int (s))
			#print ("new + :",new)

		if i in "-":
			#print (new)
			s = new.pop(1)
			f = new.pop(0)
			#print (" - ",f,s)
			new.insert(0,int(f) - int(s))
			#print ("new - :",new)

	return new

n = input()
ans = cal_1(n)
print (*ans)



