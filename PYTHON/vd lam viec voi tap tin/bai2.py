f=open('D:/input.inp.txt','r')
n=int(f.readline())
a=list(f.read().split())
print(n)
print(data)
f.close()
f1=open("D:/Out.inp.txt",'w')
dem=0
for i in range(n):
    if a.count(a[i])==1:
        print(a[i])
        dem=dem+1
if dem==0:
     f1.write('No char')
f.close()

  