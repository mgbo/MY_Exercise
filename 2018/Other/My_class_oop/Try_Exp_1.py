


try:
	f = open('testfile.txt')
	print (f.read())
except Exception as e:
	print ('Sorry. This file does not exist')
	print (e)

else:
	print (f.read())
	f.close()

finally:
	print ("Excuting Finally........")