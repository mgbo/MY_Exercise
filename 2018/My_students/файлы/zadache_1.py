

def read_num(n):
    m = []
    for i in range(n):
        line = input()
        #print('--%s--' % line)
        m.append(list(map(int, line.split())))
    return m

def transposed_M_1(m):
    transposed = []
    for i in range(4):
        transposed_row = []
        for row in m:
            transposed_row.append(row[i])
        transposed.append(transposed_row)
    return transposed

def transposed_M_2(m):
    transposed =[]
    for i in range(4):
        transposed.append([row[i] for row in m])
    return transposed

def print_Matrix(m):
    for row in m:
        for x in row:
            print (x, end=' ')
        print()

n = int(input())
Matri = read_num(n)
tran_Matri = transposed_M_1(Matri)
print_Matrix(tran_Matri)



