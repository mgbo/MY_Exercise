
# -*- coding:utf-8 -*-

import sys

rol=[]
first = []
for mark in sys.stdin:
	submark = map(str,mark.split())
	rol = rol+submark
	t = mark[0]
	first.append(t)


print first
print rol






