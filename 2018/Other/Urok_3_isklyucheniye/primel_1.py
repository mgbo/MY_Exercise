
# ------------ Первый пример ------------
'''
def foo(a):
	x = 5 / a
	print(x, a)

# try выполянется только до первого исключения, поэтому он не может работать foo(7)
try:
	foo(5)
	foo(0)      # на 0 делить нельзя
	foo(7)
except ZeroDivisionError as e:
	print('Поймали исключение!')

print('После блока обработки исключений')
'''

# ------------ Второй пример ------------

import traceback
import sys

def foo(a):
    b = [1, 2, 3]
    x = 5 / a
    y = b[a]
    print(x, a, y)

try:    
    foo(2)
    # foo(0)      # на 0 делить нельзя
    foo(7)
except (ZeroDivisionError, IndexError)  as e:
    print('Поймали исключение!')
    print(e)
    print('-'*60)
    traceback.print_exc(file=sys.stdout)
    print('-'*60)

print('После блока обработки исключений')












