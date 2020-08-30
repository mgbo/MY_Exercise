
'''
Дана последовательность, состоящая из n чисел. 
Выясните, сколько раз в ней встречается наименьшее число.
'''

n = int(input())

l = list(map(int, input().split()))

min_l = min(l)

print (l.count(min_l))

