 
# Simple Infix Expression Evaluation Using A Stack
# The expression must be fully parenthesized
# (meaning 1+2+3 must be expressed as "((1+2)+3)")
# and must contain only positive numbers
# and aritmetic operators.
# FB - 20151107

def Infix(expr):

    expr = list(expr)
    stack = list()
    num = ""

    while len(expr) > 0:
        # print ("LENGTH LIST ---> {}".format(len(expr)))
        c = expr.pop(0)

        if c in "0123456789.":
            # print ('C ---> {}'.format(c))
            num += c

        else:
            if num != "":
                stack.append(num)
                num = ""
            if c in "+-*/":
                stack.append(c)

            elif c == ")":
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                print (num1,num2,op)

                if op == "+":
                    stack.append(str(float(num1) + float(num2)))
                    print ('ADD ---> {}'.format(stack))
                elif op == "-":
                    stack.append(str(float(num1) - float(num2)))
                    print ('SUB ---> {}'.format(stack))
                elif op == "*":
                    stack.append(str(float(num1) * float(num2)))
                    print ('MULTI ---> {}'.format(stack))
                elif op == "/":
                    stack.append(str(float(num1) / float(num2)))
                    print ('DIV ---> {}'.format(stack))
    return stack

expr = "(1+(2*3))-5"

# expr = input()
print (expr)
print (Infix(expr))
# print (eval(expr))







