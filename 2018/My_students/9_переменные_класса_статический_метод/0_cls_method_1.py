class Segment1(object):
    """Класс Segment1 описывает отрезки на оси Х"""

    counter = 0 # еще не было создано ни одной окружности

    def __init__(self, start=0, finish=0):
        # Эта функция вызывается, когда мы создаем новый объект класса.
        # self - это название переменной, которая указвает на сам объект.
        self.start = start      # переменная объекта 
        self.finish = finish
        Segment1.counter += 1

    @classmethod
    def how_many(cls):
        return cls.counter

# конец класса
s1 = Segment1(2, 5)
s2 = Segment1(3, 7)

print(Segment1.how_many())          # вызов метода класса по имени класса
print(s1.how_many())                # вызов метода класса по имени класса

n_c = Segment1.how_many()
print (n_c,type(n_c))
