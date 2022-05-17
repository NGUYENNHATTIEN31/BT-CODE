class so1:
    def __init__(self,name,a,b,c,d):
        self.name=name
        self.a=a
        self.b=b
        self.c=c
        self.d=d
    def cong(self):
            return self.a+self.b+self.c+self.d
class so2(so1):
    pass           
    def tru(self):

            return self.a-self.b-self.c-self.d
t1 = so1("số", 4,6,8,9)
t2 = so2("số", 12,11,34,21)
print("tổng số =", t1.cong())
print("tổng số =", t2.cong())
print("tổng số =", t2.tru())
print("tổng số =", t1.tru())