a = int(input("Input Number: "))
b = ((a-2)*180)/a
if a <= 2:
    print("Can't make")
else:
    from turtle import*
    while True:
        forward(30)
        left(180 - b)
        
        