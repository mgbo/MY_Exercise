
s = input()

i_f = s.index('h')
i_fin = s.rindex('h')

print (i_f)
print (i_fin)

print (s[:i_f] + s[i_fin+1:])
