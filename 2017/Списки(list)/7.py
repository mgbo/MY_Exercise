
mark=map(int,raw_input().split())

print mark
print '.....'

mark.sort()
print mark

min1=mark[0]
min2=mark[1]
print min1,min2

mark.remove(min1)
mark.remove(min2)

print mark

lenn= len(mark)
summ= sum(mark)

avr=summ/lenn

print ("average mark : %d")% avr