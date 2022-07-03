n = int(input('Nhap so luong sinh vien can nhap: '))
student_list = []
for i in range(n):
    student_list.append(input('. Ten sinh vien: '))
   
find_ = input('Nhap ten sinh vien can tim: ')
print('Vi tri sinh vien: ',student_list.index(find_))
