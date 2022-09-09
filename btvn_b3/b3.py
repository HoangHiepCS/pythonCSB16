i = input("hay nhap gì đó: ")

if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
    print("la so")
else:
    print("la chu")


#cách 2:
if (i>='0' and i<= "9"):
    print("Là số")
else:
    print("Là chữ")