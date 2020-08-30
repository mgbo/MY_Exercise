# -*- coding:utf-8 -*-
import sys

for line in sys.stdin:
	s1=line.find("bomb")
	if s1!=-1:
		print ("YES")
		exit(0)
		
print ("NO")





