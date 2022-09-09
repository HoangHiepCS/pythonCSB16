a = float(input("Input number: "))
b = a % 1
if b == 0:
    print(f"{a} is an integer")
elif b != 0:
    print(f"{a} is not an integer")

#cách 2:
if int(a) == a:
    print("Là số nguyên")
elif int(a) != a:
    print("Không là số nguyên")
