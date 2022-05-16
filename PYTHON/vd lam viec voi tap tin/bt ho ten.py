f=open('d:/hoten.txt','w')
f.write('nguyen van ba\n')
f.write('ngo van ba\n')
f.write('diec van ba\n')
f.write('ha van ba\n')
f.close()
a=[]
f=open("D:/hoten.txt",'r')
f1=open("d:/ho.txt",'w')
for i in range(4):
    data=f.readline().split()
    print(data)
    f1.write(data[0])
    f1.write('\n')
    a.append(data[0])
print(a)
    


