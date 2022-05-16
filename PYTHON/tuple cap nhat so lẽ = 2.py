
a=[]
n=int(input("nhap tuple:"))

for i in range(n):
    print('a[',i,']=',end="")
    a.append(int(input()))
print ("gia tri cua list=",a)
print ("gia tri cua tuple ban đầu=",a)
newtuple=sorted(a,reverse=True)
print("tuple giam dan la=",tuple(newtuple))
for i in range(n):
    if a[i]%2==1:
        a[i]=2
tup1=tuple(a)
print("gia tri cua tuple luc sau=",tup1)
