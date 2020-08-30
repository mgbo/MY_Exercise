
# -*- coding: utf-8 -*-
f = open('bet.log', 'r')
line = f.readline()      # отдельно читаем первую строку   
while line:
    print line
    line = f.readline()  # читаем все остальные строки
f.close()
