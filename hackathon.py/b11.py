a = int(input("Input a month: "))
if a >12 or a < 1:
    print("This month doesn't exist")
else:
    if a == 1 or  a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
        print("This month has 31 days")
    elif a== 4 or a == 6 or a==9 or a == 11:
        print("This month has 30 days")
    elif a==2:
        print("This moth has 28 or 29 days")