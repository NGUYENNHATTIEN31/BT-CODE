list=[]
n=int(input("Nhập vào : "))
for i in range(0,n,1):
    print("Nhập vào phần tử thứ ", i, end="=")
    x=int(input())
    list.append(x)
print(list)
sum=0
for j in range(0,n,1):
    if(list[j]%2==1):
        sum=sum+list[j]
print(sum)