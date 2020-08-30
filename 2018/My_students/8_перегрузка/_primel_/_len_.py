
class Shoppinglist(object):
    def __init__(self, **items):
        self.items = items
        self.list_shop = ['mgmg','koko','kyawkyaw']

    def __len__(self):
        total_items = 0
        for _ in self.items:
            total_items+=1
        return total_items

    def __str__(self):
        return 'list contains items : ' + ','.join( self.items.keys())

    def __repr__(self):
        return 'list of name : \n' + '\n'.join(self.list_shop)

    def __del__(self):
        print ("object is being destroyed")

    def __add__(self, other):
        d_new = {}
        for k,v in self.items.items():
            if k not in d_new:
                d_new[k] = v
                
        for k,v in other.items.items():
            if k not in d_new:
                d_new[k] = v
            else:
                d_new[k] += v
        return d_new

wills_items =Shoppinglist(Apple= 4, Pear=5, Banna=10, orange=19)
print (len(wills_items))
print (wills_items)
wills_items.list_shop.append('makaung')
print (repr(wills_items))

wills_items2 =Shoppinglist(Apple= 4, Pear=5, Banna=10)
print (wills_items + wills_items2)
