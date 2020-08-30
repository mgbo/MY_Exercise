'''
line='Name Age Group Class Profession'
arr = line.split()
for i in range(3):
    arr.insert(2, arr[2])
print(' '.join(arr))


line=raw_input()

for arr in line[1:]:
	arr=line.split(' ')
	print arr
'''

text = 'aqwqewqewqeggghhhvvvvbvdc'
x = {'a':3, 'd':5, 'g':8}

for key in x.keys():
    text = text.replace(key, str(x[key]))

print(text)
