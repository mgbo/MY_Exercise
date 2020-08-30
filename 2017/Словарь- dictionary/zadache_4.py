
# -*- coding:utf-8 -*-

cou = []
cit = []

for i in range (int(input("ВВедете число старан и городов : "))):
	d = str(input())
	
	pair = d.split() 
	cou.append(str(pair[0]))
	print ("Country : ",str(pair[0]))

	cit.append(str(pair[1:]))
	print ("city : ", str(pair[1:]))

d = {state: cities for cities, state in zip(cit,cou)}
print ("dict : ",d)

# ---------- для вывод ------------
list2 = []

n = int(input("Number of city : "))
for j in range(n):
    city = input()
    list2.append(city)

    for key, value in d.items():
        if list2[j] in value:
            print ("MY country is ",key)

