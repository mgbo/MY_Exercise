
# -*- coding:utf-8 -*-
import sys

sum1=0

for line in sys.stdin:
	s=line.count('bomb')
	sum1+=s
	
print (sum1)
