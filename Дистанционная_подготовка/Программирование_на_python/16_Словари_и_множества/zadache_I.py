

union = set()
all = set()

for i in range(int(input())):
    m = int(input())
    a = {input() for j in range(m)} # set 
    all.update(a)
    print ('\nAll :',all)

    if len(union) == 0:
        union.update(a)
        print ("\nunion1 :",union)
    else:
        union &= a
        print ("\nunion2 :",union)



print ("------------------")
print(len(union))
print('\n'.join(sorted(union)))
print(len(all))
print('\n'.join(sorted(all)))
