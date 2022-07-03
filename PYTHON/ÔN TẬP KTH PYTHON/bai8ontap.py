import math
a=eval(input('nhập vào số a:'))
b=eval(input('nhập vào số b:'))
c=eval(input('nhập vào số c:'))
denta=(b*b)-4*a*c
print('denta=',denta)
if a==0:
    print('vui lòng nhập lại')
    
else:
   if (denta==0):
       print('phương trình có nghiệm kép x1=x2=',-b/(2*a))
   if (denta>0):
       x1=(-b+math.sqrt(denta))/(2*a)
       x2=(-b-math.sqrt(denta))/(2*a)
       print("phương trình có 2 nghiệm phân biệt x1=",(x1),";""x2=",x2)
   else:
       print('phương trình vô nghiệm')




    
