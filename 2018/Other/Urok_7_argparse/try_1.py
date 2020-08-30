
'''
a = 10
b = 0
c = a/b

'''
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)

except Exception as e:
   print("Error! " + str(e))
print("stop")


'''
except(ValueError, ZeroDivisionError):
   print("Error!")
print("stop")
'''