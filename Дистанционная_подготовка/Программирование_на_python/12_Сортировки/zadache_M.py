

razmer_konkov = sorted([int(i) for i in input().split()], reverse=True)
razmer_nogi = sorted([int(i) for i in input().split()])

for stu in razmer_nogi:
	while razmer_konkov and stu > razmer_konkov[-1]:
		s = razmer_konkov.pop()
		print ("s1 : ",s)
	try:
		s2 = razmer_konkov.pop()
	except IndexError:
		break

'''
# ------------------- vrain 1 ------------------------

skates = sorted([int(i) for i in input().split()], reverse=True)
children = sorted([int(i) for i in input().split()])
weared = 0
 
for c in children:
     while skates and c > skates[-1]:
         s = skates.pop()
         print ("s1 : ",s)
     try:
         s2 = skates.pop()
         print ("S2 : ",s2)
     except IndexError:
         break
     weared += 1


print(weared)

'''




