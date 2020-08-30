
import os

#print(dir(os))

print (os.getcwd()) #current working directory
os.chdir('/Users/myomaung/Desktop/')
print (os.getcwd())

print (os.listdir())
#os.mkdir('OS-Demo-2/myo')
#os.rmdir('OS-Demo-2/myo')
#os.mkdir('test.txt')
#os.rename('test.txt','retest.txt')
print(os.stat('retest.txt'))
