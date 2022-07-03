import string


n=input("nhập vào 1 câu:")
# d={"DIGITS":0, "LETTERS":0}
num=0
char=0
for i in n:
    if i.isdigit():
        num+=1
    elif i.isalpha():
       char+=1
    else:
        pass
print ("Số chữ cái là:", char)
print ("Số chữ số là:", num)
# def bai_1():
# string = input('Nhap vao 1 chuoi: ')
# num = 0
# char = 0
# for i in string:
#     if str.isdigit(i):
#             num += 1
#     else: char += 1
# print(f'So chu so: {num}')
# print(f'So chu cai: {char}')