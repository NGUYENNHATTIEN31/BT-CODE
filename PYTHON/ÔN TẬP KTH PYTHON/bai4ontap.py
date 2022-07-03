# ucln
def ucln(a,b):
    if(b==0):
        return a
    else:
        return ucln(b,a%b)
#bcnn
def bcnn(a,b):
    return int((a*b)/ucln(a,b))
a=int(input("nhập số a="))
b=int(input("nhập số b="))
print("ucln của a và b là ",ucln(a,b))
print("bcln của a và b là ",bcnn(a,b))


