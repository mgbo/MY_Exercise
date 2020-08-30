
'''

Задача 1
Написать одному чесловеку кодирование (шифрование), а другому - декодирование (расшифровку)


'''

apha = 'abcdefghijklmnopqrstuvwxyz' # - что было

print (apha.index('a'))

# for i,c in enumerate(apha):
# 	print(i, c)

code = ''
for letter in apha:
	code += apha[(apha.index(letter) + 3) % len(apha)]

print (code)

l = input('Write here :')

ans = ''
for i in l:
	if i in apha:
		ans += apha[(apha.index(i.lower()) + 3)%len(apha)]
	else:
		ans += i

print (ans)

