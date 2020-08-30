

""" Напишите класс Drob, который представляет дроби в виде целых числителя и знаменателя."""

class Drob(object):
    """ Дробь вида a/b """
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
        self.normalize()

        if self.b < 0:
            self.b = abs(self.b)
            self.a = -1*self.a
        elif self.b == 0:
            raise ZeroDivisionError

    @staticmethod
    def nod(a,b):
        res = 1
        while res!=0:
            res = a%b
            a,b = b ,res
        return a

    def normalize(self):
        """ Приводит дробь вида 4/6 к 2/3"""
        k = Drob.nod(self.a, self.b)        # можно self.nod
        self.a //= k
        self.b //= k

    def __str__(self):
        if self.b == 1:
            return '{}'.format(self.a)
        else:
            return '{}/{}'.format(self.a, self.b)

    def __repr__(self):
        #return '({}/{})'.format(self.a, self.b)
        return self.__str__()

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __gt__(self, other):
        return self.a * other.b > self.b* other.a

    def __add__(self, other):
        t = Drob()
        t.a = (self.a * other.b) + (self.b * other.a)
        t.b = (self.b * other.b)
        t.normalize()
        return t

    def __sub__(self, other):
        t = Drob()
        t.a = (self.a * other.b) - (self.b * other.a)
        t.b = (self.b * other.b)
        t.normalize()
        return t

    def __floordiv__(self, other):
        d_new = Drob()
        # return (self.a * other.b)//(self.b * other.a)
        d_new.a = self.a * other.b
        d_new.b = self.b * other.a

        d_new.normalize()
        return d_new

    def __truediv__(self, other):
        d_new = Drob()
        d_new.a = self.a * other.b
        d_new.b = self.b * other.a
        d_new.normalize()
        return d_new

    def __mul__(self, other):

        t_n = Drob()
        t_n.a = (self.a * other.a)
        t_n.b = (self.b * other.b)

        t_n.normalize()

        return t_n

    def __pow__(self, n):

        aa = self.a ** n
        bb = self.b ** n

        return Drob(aa,bb)

    @classmethod
    def read(cls, line):
        a, b = map(int, line.split('/'))
        new = Drob(a,b)
        return new

        # или сразу return Drob(a,b) - можно обойтись без переменной t
        #return cls(a,b)


def test():

    d1 = Drob(1,2)
    print (d1)
    d2 = Drob(3,4)
    print (d2)

    # -------------- lt ------------------------
    print (d1<d2) # True
    print (d1>d2) # False

    #---------------- gt ----------------------
    print(Drob(9,2)>Drob(5,2)) # True

    #---------------- add ---------------------
    print(Drob(5,2)+Drob(10,3)) # 35/6

    #---------------- sub ----------------------
    print(Drob(19,5)-Drob(2,3)) # 47/15

    #---------------- mul ----------------------
    print (Drob(2,4)*Drob(2,3)) # 4/12 --> 1/3

    #---------------- floordiv ------------------
    print (Drob(2,3)//Drob(2,3))

    #--------------- div ------------------------
    print (Drob(2,3)/Drob(2,3))

    #---------------- floordiv ------------------
    print (Drob(2,4)**2)

def test3():
    text = \
    '''
    1/2
    +
    1/6
    '''
    #print (text)

    for line in text:
        new = Drob.read(line)
        print (new)

def test2():
    f1 = Drob(2,-3)
    f2 = Drob(2,4)
    f3 = f1+f2

    print (f3,type(f3))
    print ("-----------")


    d1 = Drob(2,4)
    print (d1)

    d2 = Drob(2,3)
    print (d2)

    print ("ANS :",d1*d2)


    d3 = Drob(18,-2)
    print (d3)

    print ('nod : ',Drob.nod(1,5))
    print ('nod : ',Drob.nod(6,3))

    num = '1 2'
    d_1 = Drob.read(num)
    print (d_1)

    print (Drob(1,3) + Drob(1,6))

def test_clc():
    res = Drob()

    while True:
        sing = input()
        if sing == '=':
            res +=o_d
            print (res)
            break

        elif sing == '+':
            res +=o_d
            #print (res)

        elif sing == '-':
            res -= o_d

        else:
            o_d = Drob.read(sing)

if __name__ == "__main__":

    #test()
    #a,b = map(int, input().split())
    #print (nod(a,b))

    print ("-------------")

    test_clc()

    assert (test_clc()== 4/3)  # (1/2 + 1/3 + 1/2)
