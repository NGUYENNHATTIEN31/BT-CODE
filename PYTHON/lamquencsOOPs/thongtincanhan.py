class thongtincanhan:
    def __init__(self,hoten,lop,tuoi):
        self.hoten=hoten
        self.lop=lop
        self.tuoi=tuoi
    def display(self):
        print("hoten:%s\nlop:%s\ntuoi:%d\n"%(self.hoten,self.lop,self.tuoi))
ttcn1=thongtincanhan("Nguyễn Nhật Tiến","CNTT-15B",19)
ttcn1.display()

class thongtinmoi(thongtincanhan):
    pass
ttcn2=thongtinmoi("nguyen van a","CNTT-15A",18)
ttcn2.display()

