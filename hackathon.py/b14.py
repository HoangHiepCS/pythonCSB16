from audioop import reverse


while True:
    a = input("Username: ")
    b = input("Pass:")
    if len(b)>=8:
        c = input("Repeat pass:")
        if b == c:
            d = input("Email: ")
            for i in d:
                if i == "@" and i ==".":
                    print("OK!")
                    break
                else:
                    reversed
        elif b != c:
            print("Not match")
            reversed(c)
        else:
            print("Wrong! Try again")
    else:
        print("Không hợp lệ")
        reversed(b)
