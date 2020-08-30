

x=int(input())
y = int(input())
p = int(input())
i = 0
while x < y:
    x *= 1+p/100
    i += 1
print(i)


'''
x = int(input())
p = int(input())
y = int(input())
 
yearly = x * (p/100)
print ("Yearly --> ",yearly)

years = 0
 
while x < y:
    x = round(x+yearly, 2)
    print ("X --- > {}".format(x))
    years += 1
 
print(years)

'''

'''
x = int(input()) # вклад в банке
p = int(input()) # Увеличивается на p процентов
y = int(input()) # y рублей через нескоко лет


year = 1
next_year = x # for second day 


while next_year < y:
	print ('Year : {} , total money --> {}'.format(year, next_year))
	next_year += (100//p)
	year +=1

print (year)
'''
