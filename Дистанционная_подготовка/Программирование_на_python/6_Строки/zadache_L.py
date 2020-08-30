
n = input()

h1 = n.index('h')
h2 = n.rindex('h')

# print (h1, h2)

mid = n[h1+1:h2].replace('h','H')

print (n[:h1+1] + mid + n[h2:])



