
myDic={10: 'b', 3:'a', 5:'c', 0:'aa'}

sorted_list=sorted(myDic.items(), key=lambda x: x[1])

print (sorted_list)