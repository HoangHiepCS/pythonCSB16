import math
a= float(input("Nhập a:"))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
delta = b**2 - 4*a*c
if delta <0:
    print("No Vallue")
elif delta == 0:
    print(f"Phương trình có nghiệm x = {-b/(2*a)}")
else:
    x1 = ((-b - math.sqrt(delta))/(2*a))
    x2 = ((-b + math.sqrt(delta))/(2*a))
    print(f"Có 2 nghiệm {x1} và {x2}")
