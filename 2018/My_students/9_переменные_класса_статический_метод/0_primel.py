

class Drob(object):
    """ Дробь вида a/b"""
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

    @staticmethod
    def nod(x, y):      # нет self
        res = x % y
        #res = 1
        while res > 0:
            x, y = y, res
            res = x % y
        return y

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        k = Drob.nod(self.a, self.b)        # можно self.nod
        self.a //= k
        self.b //= k
    
    @classmethod
    def read(cls, line):
        a, b = map(int, line.split('/'))
        #print (a,b)
        return cls(a,b) #cls - ссылка на весь класс

    def __str__(self):
        return '{}/{}'.format(self.a, self.b)

    # реализация функций __eq__, __lt__, __add__, __sub__, __mul__,
    
    def __add__(self, other):
        t = Drob()
        t.a = (self.a * other.b) + (self.b*other.a)
        t.b = self.b * other.b
        t.normalize()
        return t

def test():
    res = Drob()
    while True:
        sing = input()
        if sing == '+':
            res +=o_d
            print (res)
        
        elif sing == '=':
            res +=o_d
            print (res)
            break
        else:
            o_d = Drob.read(sing)

if __name__ == '__main__':
    test()
    

