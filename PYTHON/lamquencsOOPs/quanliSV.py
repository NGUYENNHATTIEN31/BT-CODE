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
s=[]
n=int(input("nhập vào số sinh viên cần quản lí"))
def nhap():
    for i in range(n):
        print("nhập vào thông tin sinh viên thứ:",i+1)
        ten=input('nhập vào tên sv:')
        lop=input('nhập vào lop sv:')
        diem=float(input('nhập vào diem sv:'))
        truong=input('nhập vào truong:')

        sv=qlsv(ten,lop,diem,truong)
        s.append(sv)
nhap()
def xuat():
    i=1
    for sv in s:
        print('in ra thông tin sinh viên thứ',i)
        sv.show()
        i=i+1
    xuat()
def sapxep():
    for i in range(n):
        for j in range(n):
            if (s[i].diem<s[j].diem):
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
sapxep()
def diemmax():
    imax=0
    dmax=0
    for i in range(n):
        if s[i].diem<imax:
            imax=s[i].diem
            dmax=i
    s[dmax].show()
    # print('sinh vien co diem cao nhat';a[dmax].ten)
def xeploai():
    print('day la danh sach cac sv xep loai gioi')
    for i in s:
        if i.diem >8:
            i.show()
            
        
        
















