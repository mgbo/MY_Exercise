
import copy

class Matrix:

    def __init__(self, inp=None):
        inp = inp or []
        self.strings = len(inp[0])
        self.cols = len(inp)
        self.matr = []
        for x in inp:
            self.matr.extend(x)
        return None

    def __repr__(self):
        return '<strings = {} columns = {} matrix - {}>'.format(self.strings, self.cols, self.matr)

    def size(self):
        return (self.strings, self.cols)

    def __str__(self):
        s = ''
        for j in range(self.strings):
            s += '\t'.join(map(str, self.matr[(j) * self.cols:(j + 1) * self.cols]))
            s += '\n'
        return s

    def reshape(self, strings, columns):
        if strings * columns != len(self.matr):
            print('Действие невозможно!')
        else:
            self.strings = strings
            self.cols = columns

    def __add__(self, matr2):
        import copy
        if matr2.strings == self.strings and matr2.cols == self.cols:
            a = copy.deepcopy(matr2)
            for i in range(len(self.matr)):
                a.matr[i] += self.matr[i]
            return a
        else:
            print('Sizes of matrixes are different!')
            return 0

    def __mul__(self, const):
        a = copy.deepcopy(self)
        for i in range(len(a.matr)):
            a.matr[i] *= const
        return a

    def __rmul__(self, const):
        return self.__mul__(const)
        
if __name__ =='__main__':
    m = Matrix([[1, 2], [4, 5], [6, 4], [2, 2]])
    n = Matrix([[1, 2], [4, 5], [6, 4], [2, 2]])
    a = 3
    print(repr((m)))
    print(m+n)
    print(str(m)==str(n))
    print(a*n)
