a=[]
n=int(input("nhap vao so phan tu="))

for i in range(n):
    print('a[',i,']=',end="")
    a.append(int(input()))
print ("gia tri cua list=",a)

tup1=tuple(a)
print("gia tri cua tuple=",tup1)

b=sorted(tup1)
print(b)

tup2=tuple(b)
print(tup2)
#nhap vao tuple(so nguyen)vao ban phím gom các so chan và so lẽ thay các so lẽ của tuple dó = so 0