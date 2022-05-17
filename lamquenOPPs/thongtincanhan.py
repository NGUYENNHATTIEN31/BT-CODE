class thongtincanhan:
    def __init__(self,hoten,lop,tuoi):
        self.hoten=hoten;
        self.lop=lop;
        self.tuoi=tuoi;
    def display(self):
        print("hoten:%s \n lop:%s \n tuoi:%d \n"%(self.hoten,self.lop,self.tuoi))
ttcn1=thongtincanhan("Nguyễn Nhật Tiến","CNTT15B",19)
ttcn1.display();
