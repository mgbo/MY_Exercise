
f = open('file_B.txt', 'r')

str = f.read() # прочитать весь файл в переменную str
print (str)

s_str = str.split()
print (s_str)

ans = [int(i) for i in s_str]

print ("ans : ",sum(ans))
f.close()