

# n = float(input())
# nn = float(n - int(n))
# print (nn)


# v1
# a = 1.45678
# b = float('0.%s' % str(a).split('.')[1])
# print (b)

# v2
a = input()
b = float('0' + a[a.index('.'):])
print (b)