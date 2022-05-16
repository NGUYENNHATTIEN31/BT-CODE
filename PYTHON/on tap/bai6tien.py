from asyncore import write
from encodings import utf_8


# f=open("D:/data.txt",'w',encoding='utf_8')

# f.write('CĐ-CNTT15B')
# f.write('\n')
# f.write('NGUYỄN NHẬT TIẾN')
# f.write('\n')
# f.write('15 tuổi')
# f.write('\n')
# f.write('tienduje@gmail.com')
# f.write('\n')
# f.write('326/32/10A-LÊ HỒNG PHONG')
# f.close()

f=open('d:/data.txt','r',encoding="utf8")
content=f.read()
print(content)
f.close()