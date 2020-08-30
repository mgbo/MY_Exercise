
# sashnat. Lists
# «Больше своих соседей» "Greater than its neighbors"
# Дан список чисел. 
# Определите, сколько в этом списке элементов, которые больше двух своих соседей, и выведите количество таких элементов. 
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.


'''
a = input().split() # список строк
m = 0
for i in range(1, len(a)-1):
    if int(a[i-1]) < int(a[i]) and int(a[i]) > int(a[i+1]):
        m += 1
print(m)

'''

l = list(map(int,input().split()))

num = 0

for i in range(1,len(l)-1):
	if int(l[i-1]) < int(l[i]) and int(l[i]) > int(l[i+1]):
		print (l[i])
		num+=1

print (num)





