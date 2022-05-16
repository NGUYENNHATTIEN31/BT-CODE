print(abs(-45))
import math
print(math.ceil(5.25))
print(math.exp(3))
print(math.fabs(-15))
print(math.floor(5.25))
print(math.log(5))
print(max(20,52,15))
print(min(23,5,15))
# randrage(2,15,2)->2->14
import random
print(random.randrange(1,100,1))
print(random.randrange(20))


chuoi= "tienxinhtraipro123"
chuoi_tim="pro"
print(chuoi.center(30,"♥"))

print(chuoi.count("n",0,11))

print(chuoi.find((chuoi_tim)))

print(chuoi.find(chuoi_tim,3,15))

#
import time
print (time.time())
print(time.localtime(time.time()))

#
n=int(input())
a=[]
for i in range(n):
    print("vui long nhap phan tu thu ",i,end= "=")

    x=int(input())
    a.append(x)
print(a)
a.insert(n,100)
print(a)
print(a.count(3))

b=[100,200,300]
a.extend(b)
print(a)

print(a.index(100))

