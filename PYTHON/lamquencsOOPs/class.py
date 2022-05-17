class tugiac:
    def __init__(self,name,a,b,c,d):
        self.name=name
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def chuvi(self):
        return self.a+self.b+self.c+self.d

class binhhanh(tugiac):
    pass

    def dientich(self):
        return self.a*self.b
tg1 = tugiac("tứ giác", 4,7,10,3)
print("chuvi tứ giác", tg1.chuvi())

bh1= binhhanh("bình hành", 4,7,4,7)
print("chuvi hình bình hành", bh1.chuvi())
print("Diện tích bình hành", bh1.dientich())

print("Diện tích tứ giác", tg1.dientich())  