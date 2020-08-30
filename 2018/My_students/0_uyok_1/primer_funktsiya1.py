
#-*- coding:utf-8 -*-

def height(h):
	m = h//100
	sm = h%100
	return m,sm

mym,mysm = height(169)

print ("мой рост %d метров %d сантиметров"%(mym,mysm))

you = int(input())

ym,ysm = height(you)

print ("мой рост %d метров %d сантиметров"%(ym,ysm))
