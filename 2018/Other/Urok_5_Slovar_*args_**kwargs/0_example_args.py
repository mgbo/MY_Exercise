
"""
под произвольным числом здесь понимается ситуация, когда вы
не знаете заранее сколько аргументов может быть передано фукции
пользователем, поэтому в данном случае вам необходимо использовать это
ключевые слова (*args)

*args используется для передачи произвольного числа неименованных аргументов функции.
"""


def test_var_args(f_arg, *args):
	print ("Первый позиционный аргумент : ", f_arg)
	for arg in args:
		print ("Другой аргумент из *argv : ", arg)

test_var_args('c++','Python','C#','C')

#------------------------------------------------
def test_args_kwargs(arg1, arg2, arg3):
	print ("arg1 : ", arg1)
	print ("arg2 : ", arg2)
	print ("arg3 : ", arg3)


num = ('two', 3, 5)
test_args_kwargs(*num)

print ("---------------")

# Теперь с **kwargs

num_kwagrs = {"arg3":3, "arg2":2, "arg1":1}

test_args_kwargs(**num_kwagrs)












