from calendar import TextCalendar


class Cd:
    def __init__(self,tenCD,soBh,tenCasi,giathanh) :
        self.tenCD=tenCD
        self.soBh=soBh
        self.tenCasi=tenCasi
        self.giathanh=giathanh
    def show(self):
        print(self.tenCD,'-',self.soBh,'-',self.tenCasi,'-',self.giathanh)
a=[]
n=int(input('nhập số cd'))
def nhap():
     for i in range(n):
        tenCD=input('nhập vào tên CD:')
        soBh=input('nhập vào số bài hát')
        tenCasi=input('nhập vào tên ca sĩ:')
        giathanh=float(input('nhập vào giá thành:'))
        cd=Cd(tenCD,soBh,tenCasi,giathanh)
        a.append(cd)
nhap()
def xuat():
    s=0
    for i in a:
        i.show()
        s=s+i.giathanh
        print("tổng giá thành:",s)
xuat()
while True:
    print('tiếp tục nhập:1:có :không:0')
    luachon=int(input())

    if luachon==1:
        nhap()
        xuat()
    if luachon==0:
        break
   

        
