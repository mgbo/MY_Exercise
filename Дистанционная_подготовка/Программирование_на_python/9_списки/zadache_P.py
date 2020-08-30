
l = list(map(int, input().split()))

ind_min = l.index(min(l))
ind_max = l.index(max(l))

# print (ind_max, ind_min)

l[ind_max], l[ind_min] = l[ind_min], l[ind_max]
print (*l)



