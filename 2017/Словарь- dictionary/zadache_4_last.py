
# -*- coding:utf-8 -*-

A = dict()
D = []
F = []

for n in range (int(input())):  
    F = input().split()
    print ("F is : ",F)
    key = F[0]
    #del F[0]
    val = F[1:]
    A[key] = val
  
list2 = [] # пустой список

n = int(input())
for j in range(n):
    city = input("ВВедите название города : ")
    list2.append(city)
    
    for key, value in A.items():
        if list2[j] in value:
            #print "MY country is "
            print (key)










