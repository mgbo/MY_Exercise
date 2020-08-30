
class Drob(object):
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b
      self.normalize()
    if self.b < 0:
        self.b = abs(self.b)
        self.a = -1*self.a
    elif self.b == 0:
        raise ZeroDivisionError
