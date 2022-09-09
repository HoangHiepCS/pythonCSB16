from turtle import*
a = float(input("Input length 1: "))
b = float(input("Input length 2: "))
c = float(input("Input length 3: "))
if ((a + b) <= c) or ((b + c) <= a) or ((c + a) <= b):
    print("The 3 line segments cannot form a triangle.")
else:
    if (a**2 +b**2 == c**2) or (b**2 +c**2 == a**2) or (a**2 +c**2 == b**2):
        print("The 3 line segments can form a right triangle.")
    elif a == b == c:
        print("The 3 line segments can form an equilateral triangle.")
        left(60)
        forward(a)
        right(120)
        forward(a)
        right(120)
        forward(a)

    else:
        print("The 3 line segments can form a triangle.")
