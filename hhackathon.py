# #1
# FirstName = input("First Name: ")
# LastName = input("Last Name: ")
# print(f"Your full name is {FirstName} {LastName}")
# #2
# #3
# a = float(input("Input a number: "))
# b = a ** 2
# print(b)
# #4
# a = float(input("Input circle's radius: "))
# from turtle import*
# circle(a)
# #5
# for i in range(3,13):
#     print(i)
# #6
# a = int(input("Number: "))
# for i in range (a+1):
#     print(i)
# #7
# a = int(input("Input a number: "))
# for i in range(a+1):
#     if i % 2 ==0:
#         print("")
#     else:
#         print(i)
# #8
# a = int(input("Input number of edge: "))
# b = ((a-2)*180)/a
# from turtle import*
# while True:
#     forward(40)
#     left(180-b)
# #9
# a = float(input("Input a number: "))
# if a >13:
#     print("This number is larger than 13")
# else:
#     print("This number is not larger than 13")
##10
# a = int(input("Input number: "))
# if a %2 == 0:
#     print("Chẵn")
# else:
#     print("Lẻ")
##11
# a = int(input("Input a month: "))
# if a >12 or a < 1:
#     print("This month doesn't exist")
# else:
#     if a == 1 or  a == 3 or a == 5 or a == 7 or a == 8 or a == 10 or a == 12:
#         print("This month has 31 days")
#     elif a== 4 or a == 6 or a==9 or a == 11:
#         print("This month has 30 days")
#     elif a==2:
#         print("This moth has 28 or 29 days")
##12
# a = input("Username: ")
# b = input("Pass    : ")
# c = input("Email   : ")
# if a =="admin" and b =="12345" and c =="abc@gmail.com":
#     print("OK.")
# else:
#     print("Login failed")
##13
# while True:
#     a = input("Username: ")
#     b = input("Pass:")
#     c = input("Repeat pass:")

#     if b == c:
#         d = input("Email: ")
#         print("OK!")
#         break
#     elif b != c:
#         print("Not match")
#         reversed(c)
#     else:
#         print("Wrong! Try again")
##14
# from audioop import reverse


# while True:
#     a = input("Username: ")
#     b = input("Pass:")
#     if len(b)>=8:
#         c = input("Repeat pass:")
#         if b == c:
#             d = input("Email: ")
#             for i in d:
#                 if i == "@" and i ==".":
#                     print("OK!")
#                     break
#                 else:
#                     print("Không phải 1 email")
#                     reversed
#         elif b != c:
#             print("Not match")
#             reversed(c)
#         else:
#             print("Wrong! Try again")
#     else:
#         print("Không hợp lệ")
#         reversed(b)

#bonus1
# import math
# a= float(input("Nhập a:"))
# b = float(input("Nhập b: "))
# c = float(input("Nhập c: "))
# delta = b**2 - 4*a*c
# if delta <0:
#     print("No Vallue")
# elif delta == 0:
#     print(f"Phương trình có nghiệm x = {-b/(2*a)}")
# else:
#     x1 = ((-b - math.sqrt(delta))/(2*a))
#     x2 = ((-b + math.sqrt(delta))/(2*a))
#     print(f"Có 2 nghiệm {x1} và {x2}")