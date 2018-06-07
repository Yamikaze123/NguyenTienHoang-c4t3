a = float(input("a=?"))
b = float(input("b=?"))
c = float(input("c=?"))

delta = (b**2)-(4*a*c)
A = 2*a

if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep x=", -b/A)
else:
    sqrt_delta = delta**0.5
    print("Phuong trinh co 2 nghiem")
    print("x1=",(-b-sqrt_delta)/A)
    print("x2=",(-b+sqrt_delta)/A)
