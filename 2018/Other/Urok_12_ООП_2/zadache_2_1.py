

class Rub:
    rate = 65.33
    sbig = 'руб'
    ssmal = 'коп'
    def __init__(self, r=0, kop=0):
    self.r = r + kop//100
    self.kop = kop%100

    def getRub(self):
    self.r = int(input())
    self.kop = int(input())

    def __str__(self):
    return "%d %s : %d %s"%(self.r, Rub.sbig, self.kop, Rub.ssmal)

    @classmethod
    def dol_to_rub(cls, dd):
    t_kop = (dd.d * 100 + dd.cen) * Rub.rate
    
    ch_rub = Rub(kop=t_kop)

    return ch_rub

class Dol:
    rate = 1/65.33
    sbig = 'dollar'
    ssmal = 'cent'
    def __init__(self, d=0, cen=0):
    self.d = d + cen//100
    self.cen = cen%100

    def getDol(self):
    self.d = int(input("dollar : "))
    self.cen = int(input("cents : "))

    def __str__(self):
    return "%d dollar : %d cen"%(self.d,self.cen)

    def rub_t_dol(rr): # rr - это класс Rub
    t_cen = ((rr.r*100 + rr.kop)/6533)*100
    
    dd = Dol(cen=t_cen)

    return dd

    @classmethod
    def sdache_cls(cls, pric, dol_0):
    total_cen = pric.d*100 + pric.cen # prize of icecreen to cen
    dol_new = Dol.rub_t_dol(dol_0) # rubles change to dollar

    total_cen_1 = dol_new.d * 100 + dol_new.cen

    if total_cen_1>=total_cen:
    sub = total_cen_1 - total_cen
    dol_sda = cls(sub//100,sub%100)
    print ("\nВаша сдача : ")
    print (dol_sda)
    #return dol_sda
    #return cls(sub//100,sub%100)
    Rub_sda = Rub.dol_to_rub(dol_sda)
    return (Rub_sda)			
    else:
    return ("не хватает денги")


if __name__ == "__main__":

    d1 = Dol(50,4)
    print (d1)

    r1 = Rub(130,66)
    print (r1)

    d2 = Dol.rub_t_dol(r1) # dollat to rubles
    print ("{} >>>>>>>>>>> {}".format(r1,d2))

    p1 = Dol()
    print ("Вводите цену : ")
    p1.getDol()

    ans = Dol.sdache_cls(p1,r1)
    print (ans)




