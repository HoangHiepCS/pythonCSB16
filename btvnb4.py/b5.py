from unicodedata import digit
a = int()
b = 9
if sum(digit(a)) == b and a > 1000:
    print(a)