
from  my_module import find_index,test
import sys

sys.path.append('/Users/myomaung/Desktop/my_module')


courses = ['History','Math','Physics','ComSci'] 

index = find_index(courses,'ComSci')

print (index)
print (test)

print (sys.path)

