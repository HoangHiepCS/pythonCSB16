print("Welcome to The Ultimate Security System")
a = input("Username: ")
b = input("Password: ")
if a != "admin":
    print("Wrong username or password.")
elif a == "admin":
    if b != "12345":
        print("Wrong username or password.")
    if b == "12345":
        print("You are logged in, admin.")