
'''
Только однозначных чисел

Примеры

входные данные		выходные данные
	1+2-3				0	

''' 
n = input()


def Evaluate(n):
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

ans = Evaluate(n)
print (*ans)




