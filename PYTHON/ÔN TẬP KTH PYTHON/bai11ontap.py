n=int(input("nhập vào số lượng phần tử:"))
# xuất ra danh sách phần tử đã nhập
a=[]
for i in range(n):
    print("phần tử thứ",(i+1),"la",end=" ")
    a.append(int(input()))
print (a)
#Xuất ra danh sách các phần tử theo thứ tự tăng dần
lenth=len(a)
for i in range(0,lenth-1):
    for j in range(i+1,lenth):
        if(a[i]>a[j]):
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
print("phần tử sau khi được sắp xếp")
print(a)
# Xuất ra danh sách các phần tử có giá trị chẳn.
even_num = []
for i in a:
    if i % 2 == 0:
        even_num.append(i)
print('\n', end='')
print(even_num)


