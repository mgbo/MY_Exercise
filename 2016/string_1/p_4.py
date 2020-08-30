'''
line='Name Age Group Class Profession'
arr = line.split()

for i in range(3):
    arr.insert(2, arr[2])

print arr
print(' '.join(arr))
'''

line=raw_input()
