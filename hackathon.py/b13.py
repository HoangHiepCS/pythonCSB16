while True:
    a = input("Username: ")
    b = input("Pass:")
    c = input("Repeat pass:")

    if b == c:
        d = input("Email: ")
        print("OK!")
    elif b != c:
        print("Not match")
        reversed(c)
    else:
        print("Wrong! Try again")
    