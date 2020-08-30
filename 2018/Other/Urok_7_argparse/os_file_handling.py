
import os

print (os.getcwd())

#ff = os.listdir(os.curdir)
#print (ff)

#f = open('lines.txt')

f = open('test_os.txt','w')

f.write('the first line of the text.\n')
f.write('the second line of the text.\n')

f.close()

f = open('test_os.txt')
print (f.read())

print (f.seek(0))

print (f.read())

f.close()

f = open('test_os.txt','a')
f.write('''Now is the time for all good man...)
... to come to aid of their country''')

print (f.read())













