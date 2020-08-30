
# -*- coding: utf-8 -*-

def time2min(h,m):
	mi=h*60+m
	return mi

h = int(input("часы = "))
m = int(input("минут = "))

ans = time2min(h,m)

print("переводимые часы и минуты в минуты = %d" %(ans))
