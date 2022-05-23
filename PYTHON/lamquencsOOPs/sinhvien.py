class qlsv:
    def __init__(self,ten,lop,diem,truong):
       self.ten=ten
       self.lop=lop
       self.diem=diem
       self.truong=truong
    def show(self):
        print("thông tin của sinh viên")
        print("tên sinh viên",self.ten)
        print("lớp",self.lop)
        print("điểm",self.diem)
        print("trường ",self.truong)
cd=[]
def nhap():
    n=int(input("nhập vào số sinh viên cần quản lí"))
    for i in range(n):
        print("nhập vào thông tin sinh viên thứ:",i+1)
        ten=input('nhập vào tên sv:')
        lop=input('nhập vào lop sv:')
        diem=float(input('nhập vào diem sv:'))
        truong=input('nhập vào truong:')

        sv=qlsv(ten,lop,diem,truong)
        cd.append(sv)
nhap()
def xuat():
    i=1
    for sv in cd:
        print('in ra thông tin sinh viên thứ',i)
        sv.show()
        i=i+1
xuat()





