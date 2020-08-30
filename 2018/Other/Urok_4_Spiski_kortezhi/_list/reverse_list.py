
# ------------ Вариант 1: --------------
'''
def conversely(s):
    s2 = ''
    i = len(s)-1
    while i >= 0:
        if s[i] == ' ':
            s2 = s2 + s[i+1:] + ' '
            s = s[:i]
            i = len(s) - 1
        else:
            i -= 1
    s2 = s2 + s
    return s2

string = input()
string = conversely(string)
print(string)

'''

# -------------- Вариант 2: -------------
'''
def conversely(s):
    s = s.split()
    print (s)
    s.reverse()
    print (s)
    
    s2 = ""
    
    for i in s:
        s2 += i + ' '
    return s2
 
string = input()
print (string)

string = conversely(string)
print(string)
'''


# --------- Вариант 3: --------------

def conver_l(s):
	s = s.split()
	print (s)
	s.reverse()
	print (s)
	st = ' '.join(s)
	return st

string = input()
print (string)

string = conver_l(string)
print(string)
