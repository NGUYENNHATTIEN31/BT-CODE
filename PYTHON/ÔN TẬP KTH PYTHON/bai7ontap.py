n= int(input("nhập vào số lượng phần tử trog ds:"))

a=[]
for i in range (n):
    print("nhập vào phần tử thứ:",(i+1),"là",end=" ")
    a.append(int(input()))
print("ds vừa nhập là",a)

# chan=len(a)
# for i in range (chan):
#     if(a[i]%2==0):
#      print(a[i])
#      i+=1
for i in a:
    if i%2==0:
        print(i)