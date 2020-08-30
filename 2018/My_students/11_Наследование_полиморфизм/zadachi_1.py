
class Person(object):
    def __init__(self, name, job=None, pay=0, part_time=1):
        self.name = name
        self.job = job
        self.base_pay = int(pay)
        self.part_time = float(part_time)

    def __repr__(self):
        return '{} {} {}'.format(self.name, self.job, self.pay())

    def pay(self):
        return self.base_pay * self.part_time

    def get_familiya(self):
        return self.name.split()[2]

class Teacher(Person):
    HOUR_PAY = 100
    def __init__(self, name, pay=0, part_time=0, hours=0):
        super().__init__(name=name, job='Teacher', pay=pay, part_time=part_time)
        self.hours = hours
        self.courses = set()

    def pay(self):
        res = super().pay() + int(self.hours) * Teacher.HOUR_PAY
        return res

    def add_course(self, course):
        self.courses.add(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def get_course(self):
        return self.get_familiya() + " : " + ' '.join(self.courses)

    def upgrade(self):
        self.job = 'Senior Teacher'

    @staticmethod
    def read(line):
        n, j, s, pt, h = line.split(',')

        # print('='.join([n, j, s, pt, h]))
        # print('h=<{}> {}'.format(h, type(h)), bool(h))

        if h:
            return Teacher(name=n, pay=s, hours=h)
        else:
           return Person(name=n, job=j, part_time=pt)
       
if __name__ == '__main__':

    import sys

    list_person = []

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        p = Teacher.read(line)

        print(p)
        list_person.append(p)

    print ("*"*20)

    for pp in list_person:
        print (pp.pay())
        print (pp)



    




