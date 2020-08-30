
# -*- coding:utf-8 -*-

n = input()
first = n.find('h')
final = n.rfind('h')
r = n[first+1:final].replace('h','H')
print (n[:first+1]+r+n[final:])
