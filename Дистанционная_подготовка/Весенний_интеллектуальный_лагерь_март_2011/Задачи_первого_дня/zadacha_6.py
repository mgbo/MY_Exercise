
k = int(input("Количество строк на странице : "))
n = int(input("Сумма строк : "))


l = n%k # line
p = n//k # page

if l!=0:
	print ("Нормер страницы {} , текущий строк {}".format(p+1, l))
else:
	print ("Нормер страницы {} , текущий строк {}".format(p, k))