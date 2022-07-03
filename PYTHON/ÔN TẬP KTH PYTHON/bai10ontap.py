n=int(input("nhập số nguyên dương n:"))

a=[]
for i in range(n):
    print("số thứ",i+1,end=": ")
    a.append(int(input()))
print("danh sach so nguyen vua nhap la")
print(a)

lenth=len(a)
for i in range(0,lenth-1):
    for j in range(i+1,lenth):
        if(a[i]<a[j]):
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
print(a)
print("phần tử lớn thứ 2 là")
print(a[1])
# n = int(input('Nhap so phan tu can nhap: '))
# num_list = []
# for i in range(n):
#      num_list.append(int(input(f'[{i}]: ')))
# max = num_list[0]
# for i in num_list:
#     if i > max:
#         max = i
# nd_max = num_list[0]
# for i in num_list:
#     if i > nd_max and i < max:
#          nd_max = i
# print(f'So lon thu 2: {nd_max}')

