sokm=int(input("nhap so km vào:"))
if(sokm<=1):
    sotien=15000*sokm
elif(sokm>=2 and sokm<=5):
    sotien=13500*sokm
elif(sokm>=6):
    sotien=11000*sokm
if(sokm>=120):
    giamgia = 11000*sokm/10
    sotien= (11000*sokm)-giamgia
print("so tien phai tra la:",sotien)
