class thongtincanhan:
    def __init__(self,hoten,tuoi):    
        self.tuoi=tuoi;
        self.hoten=hoten;
    def display (self):
        print("tuổi: %d \nhọtên:%s " % (self.tuoi , self.hoten))
ttcn1 = thongtincanhan("Trần Xuân Vinh", 10)
ttcn1.display();
ttcn2 = thongtincanhan("Nguyễn Quốc Huy", 12)
ttcn2.display();    
