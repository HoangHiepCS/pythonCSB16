# BUỔI 1:
# Bài 1:

# userName = input("Input your name:")
# print(f"welcome, {userName}")

#  Bài 2:

# FN = input("First Name:")
# LN = input("Last Name:")
# PN = input("Your phone number is:")
# print(f"your full name is: {FN}, {LN}")
# print(f"your phone name is: {PN}")

# num = 20
# num += int(input())
# print(num)


#Buổi 2:
#Bài 1:
# r = float(input("Hãy nhập bán kính của đường tròn:"))
# pi = 3.1416
# P = 2 * pi * r
# S = pi * r ** 2
# print(f"Chu vi đường tròn đó là {P}")
# print(f"Diện tích hình tròn đó là {S}")
#Bài 2:
# len = float(input("Lenght of edge:"))
# print(f"lenght of diagonal side: {len*2**(1/2)}")
#Bài 4:
MDY = input("Date in MM/DD/YYYY format: ")
#c1
    # print(f"Date in DD/MM/YYYY format: {MDY[3:5]}/{MDY[0:2]}/{MDY[6:]}")
#c2
x = MDY.split("/")
print(f"Date in DD/MM/YYYY format: {x[1]}/{x[0]}/{x[2]}")
