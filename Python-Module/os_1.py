
import os
from datetime import datetime

# print (dir(os))

# print (os.getcwd()) # for get current working directory


# os.chdir('/Volumes/My_Data/_python_Exercise/') # for navigate to a new loacation on the filesystem

# print (os.getcwd())

# os.mkdir('primel1') # for create new folder or file

# os.makedirs('os-Demo-2/Sub-Dir-1') # for create new folder and sub folder


# os.rmdir('primel1') # for deleting folder 
# os.removedirs('os-Demo-2/Sub-Dir-1') # for deleting folder folder and sub folder

# os.mkdir('test-1.txt')
# os.rename('test.txt', 'demo.txt') # for rename file or folder

# print (os.stat('demo.txt').st_size) # to get information

# mod_time = os.stat('demo.txt').st_mtime
# print (datetime.fromtimestamp(mod_time))


# os.chdir('/Volumes/My_Data/_python_Exercise')

# for dirpath, dirname, filenames in os.walk('/Volumes/My_Data/_python_Exercise/'):
# 	print ('Current Path : ', dirpath)
# 	print ('directories : ', dirname)
# 	print ('Files: ', filenames)
# 	print ()

print (os.environ.get('HOME'))

# print (os.listdir()) # for list directory



























