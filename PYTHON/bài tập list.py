# tính tổng các phần tử từ vị trí chẵn

from re import X


n=int(input("nhap so n"))
a=[]
for i in range(n):
    print("vui long nhap phan tu thu ",i,end= "=")

    x=int(input())
    a.append(x)
print(a)
s=0
for i in range(n+1):
   if i%2==0:
        s+=i
        i+=i
print(s)
# Tính tổng các phần tử là số lẻ trong list
n=int(input("nhap so n"))
a=[]
for i in range(n):
    print("vui long nhap phan tu thu ",i,end= "=")

    x=int(input())
    a.append(x)
print(a)
s=0
for j in range(0,n,1):
    if(list[j]%2==0):
        s=s+list[j]
        j+=1
print(s)