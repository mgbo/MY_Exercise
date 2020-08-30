
'''
Отсортируйте список прибывающих рейсов по времени прибытия и напечатайте его по формату 
старт время_в_пути стоп
'''

class Time(object):
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m
        self.validate()


    def validate(self):
        self.h +=self.m//60
        self.h %=24
        self.m = self.m % 60

    def __str__(self):
        return '{}:{}'.format(self.h, self.m)

    def total_minutes(self):
        return self.h*60 + self.m

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
        return self.__str__()

def read_time(line):
    h, m = map(int, line.split(':'))
    return Time(h,m)

def read_flight(line):
    star, dt = line.split()
    return Flight(read_time(star), read_time(dt))

def vremeni_pribytiya(line):
    return line[0]

def testTime():
    t = Time(9,45)

    t1 = Time(6,20)

    print (t+t1)

if __name__ == '__main__':
    import sys
    list_board = []

    #testTime()

    for line in sys.stdin:
        line = line.strip()
        
        if not line:
            continue

        raspisaniya = read_flight(line)
        #print (raspisaniya)

        list_board.append(raspisaniya)

    # print (list_board)
    # print (list_board[1])

    sort_list = sorted(list_board, key=lambda f: f.dt, reverse=True)

    for s in sort_list:
        print (s)

   


















