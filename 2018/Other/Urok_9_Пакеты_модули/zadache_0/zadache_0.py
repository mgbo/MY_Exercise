
def is_balanced(text, brackets="()[]{}<>"):

    for left, right in zip(brackets[::2], brackets[1::2]):
        assert left != right, "the bracket characters must differ"

    left = brackets[::2]
    print (left)
    right = brackets[1::2]
    print (right)
    
    print('left = {} and right = {} '.format(left, right))
    stack = []
    
    for c in text:
    	if c in left:
    		stack.append(c)
    		#print ('stack : ',stack)
    	elif c in right:
            stack.pop()
            if c not in stack:
                print ("больше нет")
                break
            '''
            if len(stack)>0:
                stack.pop()
            else:
                return 0
            '''

    return stack
