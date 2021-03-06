
'''
with .. as
Программисты иногда забывают закрывать файлы. Это плохо.
Если пока мы пишем произошла в программе ошибка, то программа закончит работать,
но сама файл не закроет.

Придется писать специальный код, чтобы обрабатывать ошибки. Это сложно.
Можно сделать проще - использовать конструкцию with .. as которая сама закроет файл в конце работы или если произошла ошибка:
'''
with open ('input.txt', 'r') as fin:
	for line in fin:
		print (line)
### тут файл input.txt будет уже закрыт



''' Если нужно из одного файла читать, а в другой писать, то пишут так: '''

with open('input.txt', 'r') as fin, open('output.txt','w') as fout:
	for line in fin:
		print(line, file=fout, end='')
