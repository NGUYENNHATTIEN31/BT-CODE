
n=int(input("nhập số lượng phần tử có trong mảng"))

a=[]
for i in range(n):
    print("phần tử thứ",(i+1),"la",end=" ")
    a.append(int(input()))
print("danh sách vừa nhập là",a)
# a)
tongle=0
for i in (a):
    if(i%2!=0):
        tongle+=i
        i+=1
print("tổng của số lẻ trong mảng",tongle)   
#b)
max = a[0]
for value in a:
     if value > max:
            max = value
print(f'Phan tu lon nhat: {max}')
print("nam o vi tri thu ",a.index(max))


    







