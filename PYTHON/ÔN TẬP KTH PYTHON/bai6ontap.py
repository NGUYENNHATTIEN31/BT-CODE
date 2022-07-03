from encodings import utf_8


f=open("d:/bai6.txt","w",encoding='utf_8')

f.write('CĐ-CNTT15B30')
f.write('nguyễn nhật tiến')
f.write('19 tuổi')
f.write('tienduje@gmail.com')
f.write('326/32/10A-lê hồng phong')
f.close()

f=open("d:/bai6.txt",'r',encoding="utf_8")

content=f.read()
print(content)
f.close()