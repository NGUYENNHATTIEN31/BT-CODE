#tạo set
set1={1,2,3,4,5,'one','two','three'}
print(set1)
#cập nhật và thêm mới phần tử
set1.add('four')
print(set1)
#xóa phần tử set
#discard ko có ko báo lỗi
set1.discard("four")
print(set1)
#remove ko có thì báo lỗi
# Vd: set1.remove("five")
#print(set1)

#lấy element ra khỏi set
set2=set1.pop()
print(set2)
#chiều dài,max,min,sum
print("len=",len(set1))

#print("min=",min(set1))