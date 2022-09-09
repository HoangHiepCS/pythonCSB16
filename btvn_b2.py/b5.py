a = float(input("Deposit: "))
b = (a * 105)/100
c = (b*105)/100
d = a * ((105/100)**10)
print("Lãi suất sau 1 năm là:",  b)
print("Lãi suất sau 2 năm là:",  c)
print("Lãi suát sau 10 năm là:", d)


#Cách 2:
a = 0
b = float(input("Deposit: "))
while True:
    a = a+1
    b = b*((105/100)**a)
    print(f"Lãi suất sau {a} năm là: {b}")



