
'''
def swap(a):
    a[0], a[1] = a[1], a[0]

a = [7, 9, -3, 47, 2, 1, 17]
swap(a)
print(a)                      # [9, 7, -3, 47, 2, 1, 17]
'''

def Swap1(a):
	a[0], a[-1] = a[-1], a[0]

n = list(map(int,input().split()))

Swap1(n)

print (*n)
