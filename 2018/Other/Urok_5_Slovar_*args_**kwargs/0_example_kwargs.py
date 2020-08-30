
"""
**kwargs позволяет вам передавать произвольное число именованных аргументов
в функцию. Таким образом, вам необходимо использовать **kwargs там, где вы хотите рабоать
с именованными аргументоами.
"""

def greet_me(**kwargs):
	for key,value in kwargs.items():
		print ("{0} : {1}".format(key,value))


greet_me(name="yasoob",age=14)