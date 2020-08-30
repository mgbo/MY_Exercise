
s = input()

i_f = s.index('h')
i_fin = s.rindex('h')

#print (i_f)
#print (i_fin)

rev = s[i_f:i_fin]
print (rev)

print (s[i_fin:i_f:-1])

print (s[:i_f] + rev + s[i_fin+1:])