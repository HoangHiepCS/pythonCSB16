a = int(input("Input number: "))
b = 1
if a == 0:
    print("1")
elif a >0:
    for i in range(1,a+1):
        b = b*i
    print(b)
