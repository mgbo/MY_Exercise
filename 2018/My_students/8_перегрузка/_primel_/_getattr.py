
class Frob:
    def __init__(self, bamf):
        self.bamf = bamf

    def __getattr__(self, name):
        return 'Frob does not have {} attribute'.format(str(name))

f = Frob('car')
print (f.bar)

print (f.bamf)
