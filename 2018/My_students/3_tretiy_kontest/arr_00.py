
n = int(input())
num = list(map(int,input().split()))

print (*num*2)

'''
a_1 = [num[i] for i in range(n) if num[i]%2==0]
a_2 = [num[i] for i in range(n) if num[i]%2!=0]

a_1 = [x for x in num if x%2 == 0]
print (*a_1)
print (*a_2)
'''

