
class Time:
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m
        self.validate()

    def total_minutes(self):
        return self.h*60 + self.m

    def validate(self):
        #if self.h>=24 or self.m>60:
        self.h += self.m // 60
        self.h %= 24
        self.m = self.m % 60

    def __repr__(self):
        return '{:02}:{:02}'.format(self.h, self.m)

    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()

    def __add__(self, other):
        new = Time(self.h + other.h, self.m + other.m)
        return new

class Flight():
    def __init__(self, star, dt):
        self.star = star
        self.dt = dt
        self.end = self.star + self.dt

    def __str__(self):
        return '{} {} {}'.format(self.star, self.dt, self.end)

    def __repr__(self):
        return self.__repr__()


def read_flight(line):
    star, dt = line.split()
    return Flight(read_time(star), read_time(dt))

def read_time(line):
    h, m = map(int, line.split(':'))
    return Time(h,m)

def test():
    t = read_time('16:150')
    t1 = read_time('7:05')
    print (t , t1 , t+t1)

    a = [t, t1, t+t1]
    print(a)
    a.sort()
    print(a)

def test_1():
    # f = Flight(read_time('13:45'),read_time('3:4'))
    # print (f)

    with open('output.txt','w') as fout, \
        open('imfor.txt', 'r') as f: 
        for line in f:
            line = line.strip()
            #print ('Line :',line)
            if not line:
                continue
            raspisaniya = read_flight(line)
            print (raspisaniya, file=fout)

    f.close()
    

if __name__ == "__main__":
    #test()
    test_1()

    def file_len(fname):
        with open (fname) as f:
            for i, l in enumerate(f):
                pass
            return i+1

    len_file = file_len('imfor.txt')
    print (len_file)




