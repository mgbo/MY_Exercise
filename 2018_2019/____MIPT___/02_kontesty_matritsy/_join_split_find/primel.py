

# str.split(sep=None, maxsplit=-1) - разделить по sep на много частей
str = '1,2,3,'
print (str.split(','))
print(str.split(',', maxsplit=1))
print ('------------\n')


# str.partition() - разделить на 3 части - до, разделитель, после
str1 = '1,2,3,4,5'
print (str1.partition('3'))
print (str1.partition('z'))
print ('------------\n')

# строка.join(последовательность строк)

a = ['brother', 'sister', 'брат']
print ('-'.join(a))
aa = [1, 2, 3]
print ('-------\n')
# print ('='.join(a)) # так программа не выполяется
# print ('-'.join(map(lambda x:str(x), aa)))
'''
str.find(sub[, start[, end]]) - возвращает -1, если подстроки нет
str.rfind(sub[, start[, end]]) - ищет справа
'''
s = 'labc2abc3'
id_s = s.find('bc')
print (id_s)
print(s.rfind('bc'))


# задача 1, Дан путь. Вернуть имя файла
s = '/home-local/student/workspace/python_1y/myprog.py'
s0 = 'second.jpg'
s1 = '../tatyderb/hello.py'
s2 = '../tatyderb/hello.py'

print (s)

def basename(s):
	ss = s.split('/')
	return ss[-1]

print(basename(s))


# Задача 2, dirname
# Написать функцию dirname, которая по данному пути возвращает директорию.

def dirname(s):
	ss = s.split('/')
	s3 = '/'.join(ss[:-1])
	return s3

print (dirname(s))
print (dirname(s0))
print (dirname(s1))

# Задача 3, splitext
# Написать функцию splitext, которая возвращает список из имени файла и его расширения

def splitext(s):
	l = []
	ss = s.rfind('.')
	l.append(s[:ss])
	l.append(s[ss:])
	return l

print (splitext(s0))

# Задача 4, resolve
# Нужно соединить 2 пути.

def resolve(s1, s2):
	s = s1 + s2
	print (s)
	# return s

resolve('/home-local/student/', 'workspace')
resolve('/home-local/student/workspace/ivan', '../lee')







