
f=open('D:/input.txt','r')
n = int(f.readline())
data = f.readline().split()
a=[]
for i in data:
    a=a+ [int(i)]    
print(n)    
print(data)
f.close()
f=open('D:/Tongle.txt', 'w')
s=0
for i in range(n):
    if a[i]%2==1: s=s+a[i]
f. write(str(s))
f.close()
