# def phanTichSoNguyen(n):
#     i = 2;
#     listNumbers = [];
#     # phân tích
#     while (n > 1):
#         if (n % i == 0):
#             n = int(n / i);
#             listNumbers.append(i);
#         else:
#             i = i + 1;
#     # nếu listNumbers trống thì add n vào listNumbers
#     if (len(listNumbers) == 0):
#         listNumbers.append(n);
#     return listNumbers;
 
# n = int(input("Nhập số nguyên dương n = "));
# # phân tích số nguyên dương n
# listNumbers = phanTichSoNguyen(n);
# size = len(listNumbers);
# sb = "";
# for i in range(0, size - 1):
#     sb = sb + str(listNumbers[i]) + " x ";
# sb = sb + str(listNumbers[size-1]);
# # in kết quả ra màn hình
# print("Kết quả:", n, "=", sb);
check = int(input('Nhap vao 1 so: '))
prime_list = []
if check > 1:
    for i in range(2, check+1):
        while check % i == 0:
            check /= i
            prime_list.append(str(i))
print(' x '.join(prime_list))
