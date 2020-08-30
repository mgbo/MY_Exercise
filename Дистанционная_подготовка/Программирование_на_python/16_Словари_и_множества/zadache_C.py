
# -------- vrain 1 -----------
'''
f = list(map(int,input().split()))
s = list(map(int,input().split()))

same = [ j for i in f for j in s if i==j]

print (*same)
'''

print(*sorted(set(input().split()) & set(input().split()), key=int))