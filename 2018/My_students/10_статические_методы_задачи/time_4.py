
'''

Напишите функцию, которая проверяет расписание и возвращает YES, 
если расписание корректно или 
NO, если время между прибытием любых 2 рейсов будет больше, чем 20 минут. 
Вернуть YES (корректное расписание) или NO (некорректное расписание).

'''

class Time(object):
    def __init__(self, h=0, m=0):
        self.h = h
        self.m = m
        self.validate()

    def validate(self):
        self.h +=self.m//60
        self.h %=24
        self.m %=60

    def __str__(self):
        return '{}:{}'.format(self.h, self.m)

    def __repr__(self):
        return self.__str__()

    def total_minutes(self):
        return self.h*60 + self.m

    def __lt__(self, other):
        return self.total_minutes() < other.total_minutes()

    def __add__(self, other):
        new = Time(self.h + other.h, self.m + other.m)
        return new

    def __sub__(self, other):
        t = self.total_minutes()
        t1 = other.total_minutes()

        dt = t - t1

        return (Time(dt//60, dt%60))

class Flight():
    def __init__(self, start, dt):
        self.start = start
        self.dt = dt
        self.end = self.start + self.dt

    def __str__(self):
        return '{} {} {}'.format(self.start, self.dt, self.end)

    def __repr__(self):
        return self.__str__()

def read_time(line):
    h,m = map(int, line.split(':'))
    return Time(h,m)

def read_flight(line):
    start, dt = line.split()
    return Flight(read_time(start), read_time(dt))

def test():
    t = Time(16,5)
    t2 = Time(11,35)

    print (t-t2)


if __name__ == '__main__':
    # test()

    import sys
    list_flight = []

    for line in sys.stdin:

        line = line.strip()

        if not line:
            continue

        raspisaniye = read_flight(line)

        list_flight.append(raspisaniye)

    print (list_flight)

    fisrt_f = list_flight[0].end
    print ('fisrt_flight arrival :',fisrt_f)
    print ('-'*30)

    for l in list_flight[1:]:
        second_fight = l.end

        print (fisrt_f)
        print (second_fight)

        print ('-'*30)
        if fisrt_f.total_minutes() - second_fight.total_minutes() > 20:
            pass

        else:
            print ('NO')
            break

        #print ('-'*30)
        fisrt_f = second_fight

    else:
        print ('YES')

        

















