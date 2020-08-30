
# -*- coding: utf-8 -*-

s = float(input("Площадь комнаты : "))
ln = float(input("длинла одной стороны комнаты : "))

otherside = s/ln
print ("другой стороны комнаты = %.02f"%(otherside))

ch = float(input("ширина стула : "))

res = otherside/ch

print ("поставляемые стуля = %d " %(res))
