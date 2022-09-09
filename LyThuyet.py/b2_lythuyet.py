# statement
# a = 11
# b = 10
# if a>b:
#     print("a lon hon b")
# elif a<b:
#     print("a<b")
# else:
#     print("a=b")


# a = ""
# if bool(a) == True:
#     print(a)
# else:
    # print("truong hop nay bool(a) == False")

#cách 1
# a = input("nhap so thu nhat: ")
# b = input("nhap so thu hai : ")
# c = input("nhap so thu ba  : ")
# if a == max(a,b,c):
#     print("a la so lớn nhất")
# elif b == max(a,b,c):
#     print("b la so lon nhat")
# else:
#     print("c là so lơn nhất")


# cách 2

# a = int(input("nhap so thu 1:"))
# b = int(input("nhap so thu 2:"))
# c = int(input("nhap so thu 3:"))
# if a > b and a>c:
#     print(f"{a} is max")
# elif b>a and b>c:
#     print(f'{b} la so lon nhat')
# elif c>a and c>b:
#     print(f'{c} is max')
# elif a == c and b == c:
#     print(" ba so nay bang nhau")
# elif a == c and b!=c:
#     print("số 1 bằng số 3")



# a = int(input(" Năm nay là năm bao nhiêu :"))
# if bool(a/4) == True and bool(a/100) == False:
#     print("Đây là năm nhuận")
# elif bool(a/400) == True:
#     print("Đây là năm nhuận")
# elif bool(a/4) == False:
#     print("Đây không phải là năm nhuận")
# elif bool(a/100) == True and bool(a/400) == False:
#     print("Đây không phải là năm nhuận")