# import math
# def isPrimeNum(n):
#     if n < 2:
#         return False
#     tg = int(math.sqrt(n))
#     for i in range(2, tg + 1):
#         if (n % i) == 0:
#             return False
#     return True
# n=int(input("nhập số n:"))

# if n >= 2:
#     print(2)
#     for i in range(3, n + 1):
#         if isPrimeNum(i):
#             print(i, end=" ")
#         i = i + 2
n= int(input("nhập N:"))
for i in range(2,n+1):
    dem=0
    for j in range(2,n+1):
        if i%j == 0:
            dem+=1
    if dem==1:
        print(i)


    